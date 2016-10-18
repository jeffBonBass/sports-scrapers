#!/usr/bin/env python

import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.usatoday.com/sports/nfl/sagarin/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup( html )
div = soup.find( 'div', attrs={'class': 'sagarin-page'} )

pre = div("pre")[1]

for tag in pre:
	if tag.string:
		#if tag.string.startswith( '&nbsp;'):
		#if "DIVISION AVERAGES" in tag.string:
		if "this output" in tag.string:
			break
		print tag.string.replace('&nbsp;','')

