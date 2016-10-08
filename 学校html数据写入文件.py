#!/usr/bin/env/python
# -*- coding: utf-8 -*-
####################
#编写Hello World脚本，在系统环境中执行
####################
import requests
url_list = ['http://www.legalinfo.gov.cn/sfks/2005-05/27/content_143100.htm',
	'http://www.legalinfo.gov.cn/sfks/2005-05/27/content_143125.htm',
	'http://www.legalinfo.gov.cn/sfks/2005-05/27/content_143138.htm',
	'http://www.legalinfo.gov.cn/sfks/2005-05/27/content_143154.htm',
	'http://www.legalinfo.gov.cn/sfks/2005-05/27/content_143156.htm',
	'http://www.legalinfo.gov.cn/sfks/2005-05/27/content_143157.htm']
for url in url_list:
	result = requests.get(url)
	print(result.encoding)
	re_decode = result.content.decode('gbk','ignore')
	print(re_decode)
	with open('t.txt','a',encoding='utf-8') as f:
		f.write(re_decode)


