# -*- coding: utf-8 -*-
import MySQLdb
from config import Config

def db_conn(dbserver):
    '连接数据库服务器'
    conn = MySQLdb.connect(host=dbserver["host"],user=dbserver["user"], passwd=dbserver["passwd"],charset="utf8")
    return conn

def db_execute_sql(sql,db=Config.db_server[""]):
    '连接指定的数据库，并执行sql语句，返回全部结果'
    conn = db_conn(Config.db_server)
    cursor = conn.cursor()
    conn.select_db(db)
    count_result = cursor.execute(sql) #返回结果集的行数
    result = cursor.fetchall()
    return result