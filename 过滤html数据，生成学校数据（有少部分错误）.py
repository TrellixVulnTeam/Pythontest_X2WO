#!/usr/local/bin/python
# -*- coding: utf-8 -*-
s = []
co = 0
with open('t.txt','r',encoding='utf-8') as f:
	line = f.readlines()
	for i in line:
		if 'FONT' in i:
			b = str(i.split('>')[1:3]).split('<')
			if len(b)==3:
				if b[0] == "['":b.remove("['")
				if b[-1] == "/FONT']":b.pop()
				if b[-1] == "/TD']":b.pop()
				
				if len(b)==1:b=str(b).split("'")[-1]
				if type(b)==str:b=b[:5]
				if b[-1] == "/FONT', '":b.pop()
				if len(b)==1:b=b[0][2:]
				if co == 1:s.append(b);co = 0; continue
				try:
					if len(b)==5 and int(b): s.append(b); co = 1
				except ValueError as err:
					pass
	
s.pop()
s.pop()
print(s)
				
			





