# -*- coding: utf-8 -*-
import MySQLdb
class Config(object):
    # 被测系统的host url
    host_url = "http://test.o2obest.cn:8020"

    # 登录app端的用户信息
   # username = "15011356235" # 	'18810694011': '123456'； '15011296178': '123456',
    username = "18612521705" # "18612521680"
    password = "123456"
    deviceToken = "Aq2W1f_bpueK3mjhXrRWMjmYdVx7lZUpewVsOY77n3Mp" # android

    # 石化companykey
    companyKey_shihua = "874d8c821358a5e26f2524b10f43a292"

    icCardNo = '1000111100800000238' #  '1000111100000000001'
    bankcard = '6221558812340000'

    # 数据库服务器信息
    db_server= {
        'host': '115.28.87.219',
        'user': 'server',
        'passwd': '8492107',
        'db': 'server_shuchuang'
    }


'''
    # 访问接口时使用的头部信息
    request_headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Connection': 'Keep-Alive',
        'User-Agent1': 'oneCarConsumer-android/2.1.0 companyKey/ lang/zh devId/se_1058d214 devType/MI-4LTE systemVersion/Android_6.0.1',
        'User-Agent2': "Mozilla/5.0 (Linux; Android 6.0.1; MI 4LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 scApp-android-shihua/2.2.0-123 companyKey/874d8c821358a5e26f2524b10f43a292 lang/zh devId/se_1058d214 unionPay/3.1.0 devType/MI-4LTE systemVersion/Android_6.0.1",
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'X-Requested-With': 'com.shuchuang.shihua',


    }

    # 报文体中公共内容
    request_body = {
        'companyKey': '874d8c821358a5e26f2524b10f43a292',
    }

# 登录app端的用户信息
login_user = {
	'18810694011': '123456',
	'15011296178': '123456',

	}
username = "15011296178"
password = "123456"
# 测试环境可用的测试环境
host = {
	80: 'test.o2obest.cn',
	8008: 'test.o2obest.cn:8008',
	8020: 'test.o2obest.cn:8020',
	8021: 'test.o2obest.cn:8021',
	8034: 'test.o2obest.cn:8034',
	8041: 'test.o2obest.cn:8041',
	8042: 'test.o2obest.cn:8042',
	8080: 'test.o2obest.cn:8080',
	'online': 'e.o2obest.cn'
}

host_url="http://test.o2obest.cn"

# 访问接口时使用的头部信息
request_headers = {
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Connection': 'Keep-Alive',
	'User-Agent1': 'oneCarConsumer-android/2.1.0 companyKey/ lang/zh devId/se_1058d214 devType/MI-4LTE systemVersion/Android_6.0.1',
	'User-Agent2': "Mozilla/5.0 (Linux; Android 6.0.1; MI 4LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 scApp-android-shihua/2.2.0-123 companyKey/874d8c821358a5e26f2524b10f43a292 lang/zh devId/se_1058d214 unionPay/3.1.0 devType/MI-4LTE systemVersion/Android_6.0.1",
	'Accept-Encoding': 'gzip, deflate',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Upgrade-Insecure-Requests': '1',
	'Accept-Language': 'zh-CN,en-US;q=0.8',
	'X-Requested-With': 'com.shuchuang.shihua',


}

# 报文体中公共内容
request_body = {
	'companyKey': '874d8c821358a5e26f2524b10f43a292',
}

# 测试数据库配置信息
db_config = {
	'Host': 'test.o2obest.cn',
	'UserName': 'server',
	'Pwd': '8492107',
	'dbName': 'server_shuchuang'
}
'''