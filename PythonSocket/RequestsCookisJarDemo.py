#! /usr/bin/python
# _*_ coding:utf-8 _*_

#通过设置Cookisjar来模拟请求
import requests

cookies = 'q_c1=3100983117834577aa885ddffff420d8|1508902008000|1502244739000; q_c1=3100983117834577aa885ddffff420d8|1536717745000|1502244739000; _zap=6e9e6845-9fc0-4b37-bd5b-67dd33a0c163; d_c0="AFBC6BFMMQyPTjAaBdo3JOy8rY6fWTsyECE=|1502246705"; __utma=51854390.447017781.1536721519.1536721519.1536721519.1; __DAYU_PP=6UaFMniijJeYFarvQr3743186d14651e; _xsrf=OqMi45kr8NC6jqOLmPM6C90fVGjP4tZg; z_c0="2|1:0|10:1536717745|4:z_c0|92:Mi4xQXIybUF3QUFBQUFBVUVMb0VVd3hEQ1lBQUFCZ0FsVk5zY0dGWEFEblptODBRcU9UcFZkeDcwMEN0OHZaZkNISDNB|fbc3933ca449408a0479eb60e61f91d71a726199642666b00789853ca529aa11"; __utmz=51854390.1536721519.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/chexiaopang/activities; __utmv=51854390.100--|2=registration_date=20161104=1^3=entry_date=20161104=1; tgw_l7_route=8605c5a961285724a313ad9c1bbbc186; tst=r; __gads=ID=29222b691333f61f:T=1545049387:S=ALNI_MZ4dk8S2FFqvIb-i8yO93MlYW-ETg'

jar = requests.cookies.RequestsCookieJar()

headers ={
	"Host":"www.zhihu.com",
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"

}

for cookie in cookies.split(':'):
	key , value = cookie.split('=',1)
	jar.set(key,value)

r = requests.get("http://www.zhihu.com",cookie = jar,headers = headers)
print(r.text)