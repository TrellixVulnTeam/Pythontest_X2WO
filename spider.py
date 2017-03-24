#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import urllib
import re

def getResult(url):
    """ 获得url内容
    """
    result = requests.get(url)
    return result.text

def saveImage_with_requests(result):
    """ 使用requests保存页面中的图片
    """
    reg = r'src=".+\.(png|jpg|jpeg|gif)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, result)
    for img in imglist:
        with open("D:\\%s.png"%imglist.index(img), 'wb') as f:
            for chunk in img.iter_content():
                f.write(chunk)

def saveImage_with_urllib(result):
    """ 使用urllib保存页面中的图片
    """
    reg = r'src="(.+\.png|.+\.gif|.+\.jpeg|.+\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, result)
    #   如果图片地址不是以http://开头就剔除
    # for img in imglist:
    #     if not img.startswith('http://'):
    #         imglist.remove(img)
    #   如果图片地址不是以http://开头就添加域名
    # for img in imglist:
    #     if not img.startswith('http://'):
    #         imglist[imglist.index(img)] = 'http://www.cnblogs.com' + img
    # print(imglist)
    for img in imglist:
        if img.endswith('png'):
            urllib.request.urlretrieve(img, "D:\\%s.png"%imglist.index(img))
        elif img.endswith('jpg'):
            urllib.request.urlretrieve(img, "D:\\%s.jpg"%imglist.index(img))
        elif img.endswith('jpeg'):
            urllib.request.urlretrieve(img, "D:\\%s.jpeg"%imglist.index(img))
        else:
            urllib.request.urlretrieve(img, "D:\\%s.gif"%imglist.index(img))

html = getResult('http://www.cnblogs.com/fnng/p/3576154.html')

saveImage_with_urllib(html)

