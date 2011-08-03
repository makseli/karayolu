#!/usr/bin/python
import os;

ServerPort =  raw_input(" Server Port giriniz (ontanimli= 8000) : ")
if ServerPort == "": ServerPort = "8000"
print(" \n ServerPort \"" + ServerPort + "\" olarak atandi !\n ")
os.system("python manage.py syncdb")
os.system("python manage.py runserver 0:"+ServerPort)
