# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
url = "https://en.wikipedia.org/wiki/Academy_Award_for_Best_Actor"

proxies = {
  'http': 'http://172.16.114.112:3128',
  'https': 'https://172.16.114.112:3128',
}


page = requests.get(url,proxies=proxies)

html = page.content
soup = BeautifulSoup(html,'lxml')
right_table=soup.find('table', class_='wikitable sortable')

Names = []
Wiki  = []

for row in right_table.findAll("tr"):
	
	if(len(row.findAll("th"))>0):
		cells = row.find("td")
		if(cells!=None):
			a = cells.find("a")
			if(a!=None):
				Names.append(a["title"])
				Wiki.append(a["href"])
				print("Done for " + a["title"])

df=pd.DataFrame({'Name':Names, 'url' : Wiki})
df.to_csv('Names.csv', index = False, encoding = 'utf-8')