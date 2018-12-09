#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 请求数据库
import pymysql
connection = pymysql.connect(host='39.108.123.198', user='root', password='123456',
                             db='ebookdb', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    sql = "select u.email, w.address from t_walletaddress w, t_user u where w.userId = u.Id and u.email = 'zhanxueyou@msn.com'"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
