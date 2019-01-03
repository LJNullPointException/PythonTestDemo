#! /usr/bin/python
#  _*_ coding:utf-8 _*_
#抓取猫眼电影数据排行

import requests
import re

def get_one_page(url):
	response = requests.get(url)
	if response.status_code == 200:
		return response.text
	return None

def parse_one_page(html):
	result = re.findall('<dd>.*?board-index.*?>(.*?)</i>.'+
		'*?data-src=(.*?) .*?name.*?<a.*?>(.*?)</a>.*?star.*?>(.*?)</p>'+
		'.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>'+
		'(.*?)</i>',html,re.S)
	for item in result:
		yield{
			"index":item[0],
			"image":item[1],
			"title":item[2].strip(),
			"actor":item[3].strip()[3:] if len(item[3])>3 else '',
			"time":item[4].strip()[5:] if len(item[4])>5 else '',
			"score":item[5].strip() +"."+item[6].strip()
		}

def  write_to_json(content):
	whith open('result.txt','a') as f:
		print(type(json.dumps(content)))
		f.write(json.dumps(content,ensure_ascii=False,).encode('utf-8'))


def main():
	url = 'http://maoyan.com/board/4'
	html = get_one_page(url)
	for item in parse_one_page(html):
		print(item)
		write_to_json(item)

if __name__=='__main__':
	# print("niksjsajksjk ")
	main()





