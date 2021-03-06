#! /usr/bin/python
# _*_codign:utf-8 _*_

#抓取头条街拍的妹子

import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool

def get_page(offset):
	params = {
	    'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
	}

	url = 'http://www.toutiao.com/search_content/?'+urlencode(params)
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
	except Exception as e:
		return None


def get_images(json):
	if json.get('data'):
		for item in json.get('data'):
			title = item.get('title')
			images = item.get('image_list')
			for image in images:
				print(image)
				yield {
					'image':'http:'+image.get('url'),
					'title':title
				}

def save_image(item):
	print("")
	if not os.path.exists(item.get('title')):
		os.mkdir(item.get('title'))
	try:
		response = requests.get(item.get('image'))
		if response.status_code == 200:
			file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
			if not os.path.exists(file_path):
				with open(file_path,'wb') as f:
					f.write(response.content)
			else:
				print("Already Dowaloaded",file_path)
	except requests.ConnectionError:
		print("Faild to Save Image")

def main(offset):
	number = get_page(offset)
	for item in get_images(number):
		print("====="+item.get('title'))
		save_image(item)

GROUP_START = 1
GROUP_END = 20

if __name__=='__main__':
	pool = Pool()
	groups = ([x * 20 for x in range(GROUP_START,GROUP_END)])
	pool.map(main,groups)
	pool.close()
	pool.join()