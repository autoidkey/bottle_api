# -*- coding:utf-8 -*-

from bottle import route, run
from bottle import get, post, request

@route('/login',method='GET') # or @get('/login')
#http://localhost:8080/login?user=hoge&pass=fuga
def login():
	username = request.query.get('user')
	password = request.query.get('pass')

	username = "" if username is None else username
	password = "" if password is None else password

	return '''<form action="/login" method="post">
			Username: <input name="username" type="text" value="{username}"/>
			Password: <input name="password" type="password" value="{password}"/>
			<input value="Login" type="submit" />
		</form>'''.format(username=username,password=password)

@route('/login',method='POST') # or @post('/post')
def do_login():
	username = request.forms.get('username')
	password = request.forms.get('password')

	return "{username} {password}".format(username=username, password=password)

run(host='localhost',port=8080,debug=True)


'''
@route('/hello')
@route('/hello/<user>')
def hello(user="taro"):
	return "Hello {user}".format(user=user)

@route('/date/<month:re:[a-z]+>/<day:int>/<path:path>')
def date(month, day, path):
	return "{month}/{day} {path}".format(month=month, day=day, path=path)

run(host='localhost', port=8080, debug=True)
'''