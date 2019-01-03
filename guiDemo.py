#!usr/bin python3
#_*_coding:utf-8_*_
"第一个UI显示图片"
__author__="longjian"

from tkinter import *
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel=Label(self,text="Hello,world!!")
		self.helloLabel.pack()
		self.quitButton = Button(self,text="Quit",command=self.quit)
		self.quitButton.pack()

app = Application()
app.mainloop()
