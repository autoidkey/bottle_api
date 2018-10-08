# -*- coding:utf-8 -*-

from bottle import route, run
from bottle import get, post, put, delete, request, response
import json
import test_agent

test_data = {"flag":"True","test":"OK"}

@get('/test')
def return_json():
	return json.dumps(test_data)
	#return test_data

@get('/test/<element:re:[a-z]+>')
def return_specific_element(element):
	print(element)
	if element in test_data:
		print("OK")
		return test_data[element]
	else :
		response.status = 404
		return {}

@post('/test/post')
def post():
	#requestはjson形式
	print(request.params.keys())
	for key in request.params.keys():
		print("key:",key)
		if key not in test_data :
			test_data[key] = request.params[key]
			print("add_data")
	print(test_data)
	return "succeess"

@get("/agent/srmt/<theme_id:re:[0-9]+>")
def srmt_agent(theme_id):
	q_candidates = test_agent.agent(theme_id,False)
	return q_candidates
	

run(host='localhost',port=8080,debug=True,reloader=True)