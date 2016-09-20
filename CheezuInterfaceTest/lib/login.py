# coding=utf-8
import requests
from config import Config


api_url = "/api/user/shihuaAppLogin"

def login(username,password):
        login_params = {
        "CyLoginForm[client]": "android",
        "CyLoginForm[password]": Config.password,
        "CyLoginForm[rememberMe]": "1",
        "CyLoginForm[username]": Config.username,
        "companyKey": Config.companyKey_shihua,
        "https": "0",
        "ajax": "1",
        "CyLoginForm[deviceToken]": Config.deviceToken
        }
        header={
            "Accept-Encoding":"gzip",
            "User-Agent":"scApp-android-shihua/2.2.1-126 companyKey/874d8c821358a5e26f2524b10f43a292 lang/zh devId/se_d7528af7 unionPay/3.1.0 devType/MI-4LTE systemVersion/Android_6.0.1"
            }

        result = requests.post( Config.host_url+ api_url,params=login_params,headers=header)
        if result.json()['code'] == '00000':
           print ("用户 %s, 登录成功！" %(Config.username))
           return result
        else:
           print ("用户 %s 密码 %s, 登录失败！" %(Config.username,Config.password))
           return False

def get_user_session(result):
     userSession = result.cookies['USERSESSID']
     return "USERSESSID=" + userSession

def logout():
    logout_params = {
        "companyKey":	Config.companyKey_shihua ,
        "https" : 0 ,
        "ajax": 1 ,
        }
    header={
            "Accept-Encoding":"gzip",
            "User-Agent":"scApp-android-shihua/2.2.1-126 companyKey/874d8c821358a5e26f2524b10f43a292 lang/zh devId/se_d7528af7 unionPay/3.1.0 devType/MI-4LTE systemVersion/Android_6.0.1"
            }
    api_url = "/api/user/logout"
    requests.post(Config.host_url+ api_url,params=logout_params,headers=header)


def common_header():
        header={
        'Host': Config.host_url,
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MI 4LTE Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 scApp-android-shihua/2.2.1-126 companyKey/874d8c821358a5e26f2524b10f43a292 lang/zh devId/se_d7528af7 unionPay/3.1.0 devType/MI-4LTE systemVersion/Android_6.0.1',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,en-US;q=0.8',
        'Cookie': '',
        'Cookie2': '$version=1',
        'X-Requested-With': 'com.shuchuang.shihua',
        'Upgrade-Insecure-Requests': 1
         }
        return header







