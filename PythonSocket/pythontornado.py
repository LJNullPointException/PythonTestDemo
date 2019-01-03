#! /usr/bin/python
# _*_coding:utf-8_*_
#Tornado测试
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello,world!")

def make_app():
	return tornado.web.Application([(r"/",MainHandler),])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()