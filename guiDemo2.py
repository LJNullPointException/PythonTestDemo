#!usr/bin python3
#_*_coding:utf-8_*_
"gui demo2"

__author__="longjian"

from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master);
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nmaeInput = Entry(self)
		self.nmaeInput.pack()
		self.alertButton = Button(self,text="Hello",command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nmaeInput.get() or "world"
		messagebox.showinfo('Message',"Heooll,%s" %name)

app = Application()
app.mainloop()