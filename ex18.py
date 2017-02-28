# -*- coding: utf-8 -*-
#从sys库中取出argv功能
from sys import argv
#定义传递的脚本script 和 文件名称
script, filename = argv
#将文件读到txt中
txt = open(filename)

print "Here's your file %r: " % filename
#将txt读取道德文件的内容打印出来
print txt.read()
print txt.close()
print "Type the filename again: "
#将文件输入到file_name变量中
file_again = raw_input(">")
#将file_name的文件内容读取到txt_again中
txt_again = open(file_again)
#将txt_again的文件内容打印出来
print txt_again.read()
print txt_again.close()