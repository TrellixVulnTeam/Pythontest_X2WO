#!/usr/bin/env/python
# -*- coding: utf-8 -*-
import requests
import bs4
result = requests.get('http://www.sooxue.com/gaokao/yxdm/xj.html')
string = result.content.decode('gbk', 'ignore')
soup = bs4.BeautifulSoup(string, 'html.parser')
school_list = []
for i in soup.findAll('p'):
	school_list.append((i.get_text().split(' ')[0], i.get_text().split(' ')[1], 31))

with open('school.txt', 'w', encoding='utf-8') as f:
	f.write(str(school_list))
