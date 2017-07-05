#!/usr/bin/env python

#from lxml import html
import requests
from pprint import pprint
from bs4 import *
import cgitb

cgitb.enable()

a = []

page = requests.get("https://dailyalert.org")
soup = BeautifulSoup(page.content, 'html.parser')

for x in soup.find_all(['a','href']):
		li = []
		li.append(''.join(map(str, x.contents)))
        	li.append(x.get('href'))
        	a.append(li)

for i in a:
	if '<' not in i[0]:
		print i[0], "\n", i[1], "\n"
