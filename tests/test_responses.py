import requests
import pytest

from utils import *

def testEmptyGetSuccess():
	url = main_url()
	response = requests.get(url)
	assert response.status_code == 200

def testBadGetRequestFails():
	url = main_url() + "/aa/"
	response = requests.get(url)
	assert response.status_code == 404

def testGetMetadataEmptyFail():
	url = main_url() + "/metadata/"
	response = requests.get(url)
	assert response.status_code == 404

def testGetMetadataNonExistingSubjectFails():
	unexistent = "aaaa"
	url = main_url() + "/metadata/" + unexistent
	response = requests.get(url)
	errorMessage = f"Requested subject '{unexistent}' not found"
	assert response.status_code == 200
	assert response.text == errorMessage

def testGetMetadataNonExistingPropertyFails():
	unexistent = "aaaa"
	url = f"{main_url()}/metadata/{known_subjects()[0]}/properties/{unexistent}"
	response = requests.get(url)
	errorMessage = f"Requested property '{unexistent}' not found"
	assert response.status_code == 200
	assert response.text == errorMessage

@pytest.mark.parametrize("deprecatedProperty", deprecated_properties())
def testGetMetadataDeprecatedPropertyFails(deprecatedProperty):
	url = f"{main_url()}/metadata/{known_subjects()[0]}/properties/{deprecatedProperty}"
	response = requests.get(url)
	errorMessage = f"Requested property '{deprecatedProperty}' not found"
	assert response.status_code == 200
	assert response.text == errorMessage

def testPostMetadataQueryEmptyPayloadFails():
	url = main_url() + "/metadata/query"
	response = requests.post(url)
	assert response.status_code == 500

def testPostMetadataQueryPayloadWithNoSubjectFails():
	url = main_url() + "/metadata/query"
	dataObject = {'aaa': []}
	data = json.dumps(dataObject)
	response = requests.post(url, data=data)
	assert response.status_code == 500

def testPostMetadataQueryBadStructureFails():
	url = main_url() + "/metadata/query"
	dataObject = {
		'subjects': known_subjects()[0],
		'properties' : 'aaa'
		}
	data = json.dumps(dataObject)
	response = requests.post(url, data=data)
	assert response.status_code == 500
