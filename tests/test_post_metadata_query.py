import pytest

from utils import *

def testPostMetadataQueryEmptySubjects():
	response = postMetadata([])
	assert empty_post_query_response() == json.loads(response.text)

def testPostMetadataQueryUnexistingSubjects():
	response = postMetadata(['aaa'])
	assert empty_post_query_response() == json.loads(response.text)

def testPostMetadataQueryUnexistingSubjectWithExistingSubject():
	response1 = postMetadata([known_subjects()[0], 'aaa'])
	response2 = postMetadata([known_subjects()[0]])
	assert response1.text == response2.text

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def testPostMetadataQueryUnexistingProperty():
	response = postMetadata([known_subjects()[0]], ['aaa'])
	rsp_json = json.loads(response.text)['subjects'][0]
	assert intersection(list(rsp_json.keys()), known_properties()) == []

@pytest.mark.parametrize("property", known_properties())
def testPostMetadataQueryManySubjectsOneProperties(property):
	response = postMetadata(known_subjects(), [property])
	subjects = json.loads(response.text)['subjects']
	for s in subjects:
		assert list(s.keys()).sort() == (unknown_properties() + [property]).sort()

def testPostMetadataQueryManySubjectsManyProperties():
	properties = known_properties()[0:2] + unknown_properties()[0:1]
	response = postMetadata(known_subjects(), properties)
	subjects = json.loads(response.text)['subjects']
	for s in subjects:
		assert intersection(list(s.keys()), known_properties() + unknown_properties()).sort() == properties.sort()
