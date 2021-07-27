import pytest

from utils import *

testdata = [(s,p) for s in known_subjects() for p in ([None]+known_properties()+unknown_properties())]

@pytest.mark.parametrize("subject, property", testdata)
def testGetMetadata(subject, property):
	metadata = getMetadata(subject, property)
	if property:
		if isinstance(metadata, dict):
			assert list(metadata.keys()).sort() == ['sequenceNumber', 'value', 'signatures'].sort()
		else:
			assert property in ['subject', 'policy']
	else:
		assert list(metadata.keys()).sort() == (known_properties() + unknown_properties()).sort()

def testGetMetadataCompareFullResponse():
	subject = '2048c7e09308f9138cef8f1a81733b72e601d016eea5eef759ff2933416d617a696e67436f696e'
	response = getMetadata(subject)
	assert response == getExpectedMetadata(subject)


def testGetMetadataPropertiesCompareFullResponse():
	subject = "919e8a1922aaa764b1d66407c6f62244e77081215f385b60a62091494861707079436f696e"
	prop = "decimals"
	response = getMetadata(subject, prop)
	assert response == getExpectedMetadata(subject+'-'+prop)

