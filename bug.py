import urllib.request as urllib2
import urllib.parse

def getMethod():
	url = "http://www.baidu.com"
	response = urllib2.urlopen(url)
	print(response.read())

def postMethod():
	url = "http://www.baidu.com"
	form = {'name':'abc' ,'password':'1234'}
	form_data = urllib.parse.urlencode(form)
	request = urllib2.Request(url,form_data)
	response = urllib2.urlopen(request)
	print(response.read)

postMethod()
