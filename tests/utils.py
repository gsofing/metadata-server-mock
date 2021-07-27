import requests
import json


def main_url():
	return "http://metadata-server-mock.herokuapp.com"

def known_subjects():
	return [
	'2048c7e09308f9138cef8f1a81733b72e601d016eea5eef759ff2933416d617a696e67436f696e',
	'919e8a1922aaa764b1d66407c6f62244e77081215f385b60a62091494861707079436f696e'
	]

def known_properties():
	return ["name", "description", "ticker", "logo", "url"]

def unknown_properties():
	return ["subject","decimals","policy"]

def deprecated_properties():
	return ["unit"]


def empty_post_query_response():
	return {"subjects":[]}

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

def postMetadata(subjects, properties=None):
	url = main_url() + "/metadata/query"
	dataObject = {'subjects': subjects}
	if properties:
		dataObject['properties'] = properties
	data = json.dumps(dataObject)
	return requests.post(url, data=data)
