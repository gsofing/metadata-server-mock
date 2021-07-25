import pytest
import requests
import json


def main_url():
	return "http://metadata-server-mock.herokuapp.com"

########################################################################
########################################################################

def getMetadata(subject, property=None):
	url = main_url() + "/metadata/" + subject + (("/properties/" + property) if property else '')
	response = requests.get(url)
	return json.loads(response.text)


def getExpectedMetadata(subject):
	t = ''
	with open('./testData/' + subject) as f:
		for val in f.readlines():
			t += val
	return json.loads(t)

def testGetMetadata():
	subject = '2048c7e09308f9138cef8f1a81733b72e601d016eea5eef759ff2933416d617a696e67436f696e'
	response = getMetadata(subject)
	assert response == getExpectedMetadata(subject)


def testGetMetadataProperties():
	subject = "919e8a1922aaa764b1d66407c6f62244e77081215f385b60a62091494861707079436f696e"
	prop = "decimals"
	response = getMetadata(subject, prop)
	assert response == getExpectedMetadata(subject+'-'+prop)

########################################################################
########################################################################

def postMetadata(subjects, properties=None):
	url = main_url() + "/metadata/query"
	dataObject = {'subjects': subjects}
	if properties:
		dataObject['properties'] = properties
	data = json.dumps(dataObject)
	return requests.post(url, data=data)


def testPostQuery():
	subjects = ["789ef8ae89617f34c07f7f6a12e4d65146f958c0bc15a97b4ff169f16861707079636f696e", "789ef8ae89617f34c07f7f6a12e4d65146f958c0bc15a97b4ff169f1"]
	response = postMetadata(subjects)
	assert response.status_code == 200


def testPostQueryWithProperties():
	subjects = ["789ef8ae89617f34c07f7f6a12e4d65146f958c0bc15a97b4ff169f16861707079636f696e",
		"789ef8ae89617f34c07f7f6a12e4d65146f958c0bc15a97b4ff169f1"
		"94d4cdbcffb09ebd4780d94f932a657dc4852530fa8013df66c72d4c676f6f64636f696e"]
	properties =  ["name", "description", "url"]
	response = postMetadata(subjects, properties)
	assert response.status_code == 200


