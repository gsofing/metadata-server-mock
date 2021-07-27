import pytest
from nacl.signing import VerifyKey
import binascii

from utils import *

def verify_signature(pubkey, value, signature):
	verify_key = VerifyKey(binascii.unhexlify(pubkey))
	verify_key.verify(value.encode("utf-8"), binascii.unhexlify(signature))


allMetadatas = json.loads(postMetadata(known_subjects()).text)
subjects_and_properties = []
for s in allMetadatas['subjects']:
	for k in s.keys():
		if isinstance(s[k], dict):
			subjects_and_properties += [(s['subject'], s[k])]

@pytest.mark.skip
@pytest.mark.parametrize("subject,property", subjects_and_properties)
def testPropertySignature(subject, property):
	v      = property['value']
	for signature in property['signatures']:
		pubkey = signature['publicKey'].encode("utf-8")
		sig    = signature['signature'].encode("utf-8")
		try:
			verify_signature(pubkey, v, sig)
			assert True
		except Exception as e:
			assert False

