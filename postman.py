import requests
import json
'''
url = "http://localhost:8080/test/post"
request_para = {
	'id' : 1,
	'text' : "test message"
}
res = requests.post(url, request_para)

print(res)
'''

url = "http://localhost:8080/agent/srmt"
themeid = "/19"

res = requests.get(url+themeid)
print(res.json())
