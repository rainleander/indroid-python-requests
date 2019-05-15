#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# https://github.com/rainleander/indroid-python-requests

# Junior Application Developer at indroid
# 1. Make a function which accepts a string and returns the Google-results
# for this string. You can use Python and the requests-module. 

import requests

url = 'http://google.nl'
prompt = '> '

print "What would you like to search for?"
q = raw_input(prompt)

print "How many results would you like to see?"
num = raw_input(prompt)

google = { 'q' : q, 'num' : num }

try:
	r = requests.get(url=url, params=google)
except requests.exceptions.RequestException as e:
	print e
	sys.exit(1)

print(r.url)
