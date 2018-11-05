from urllib import parse
from urllib import request
import os

#电信  为telecom
#移动  为cmcc
#联通  为 空
#类型
type = 'cmcc'
#请在分号中输入你的账号
account = ''
#请在分号中输入你的密码
password = ''

header = {
          'Origin':'http://172.16.255.253',
          'Host':'172.16.255.253',
          'Cookie':'program=test; vlan=0; ip=172.16.40.172; ISP_select=@cmcc; md5_login2='+account+'@'+type+'%7C'+password,
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
          'Cache-Control':'max-age=0'    
          }

def logIn():
    
    header['Refer'] = 'http://172.16.255.253/a70.htm'
    
    posturl = 'http://172.16.255.253/a70.htm'
    postdata = {
                'DDDDD': account+'@'+type,
                'upass': password,
                'R1': '0',
                'R2': '',
                'R3': '0',
                'R6': '0',
                'para': '00',
                '0MKKey': '123456',
                'buttonClicked': '',
                'redirect_url': '',
                'err_flag': '',
                'username': '',
                'password': '',
                'user': '',
                'cmd': '',
                'Login':''
            }
#    posturl,postdata,headers=header,'172.16.255.253',method='POST'
    post_data = parse.urlencode(postdata).encode(encoding='utf_8')
    req = request.Request(posturl,data=post_data,headers=header,method='POST')
#    print(postdata)
    responseRes = request.urlopen(req)
    if responseRes.getcode() == 200:
        print('200 OK succeed in logging in')
    
        
def logOut():
    header['Referer'] = 'http://172.16.255.253/1.htm'
    
    get_URL = 'http://172.16.255.253/F.htm'
    
    req = request.Request(get_URL,headers = header,method='GET')
    responseRes = request.urlopen(req)
    if responseRes.getcode() == 200:
        print('200 OK succeed in logging out')

def connect_to_connection():
    url = 'www.baidu.com'
    backinfo = os.system('ping -w 1 %s'%url) 
#    ping百度，如果有网则返回 0，没网则返回1
    if backinfo == 1:
        logIn()
    else:
        logOut()
    
    
if __name__ =='__main__':
    connect_to_connection()
    input('请回车结束')
    
    
 