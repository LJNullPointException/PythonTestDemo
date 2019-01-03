#! /usr/bin/python
# _*_ coding:utf-8_*_

#抓取知乎---发现页面

import requests
import re

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore",headers = headers)
patten  = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles = re.findall(patten,r.text)
print(titles)