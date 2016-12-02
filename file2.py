# -*- coding: utf-8 -*-
# 读取html文档
content = ''
with open('2016-12-02.html', encoding='utf-8') as f:
    for num, line in enumerate(f):
        if 197 >= num + 1 >= 190:
            content += line
print(content)