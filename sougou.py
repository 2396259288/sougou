#!/usr/bin/python 

# -*- coding: utf-8 -*-


import requests
from lxml import etree
import time, os, re, json, random
session = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


#获取标签Id
response = requests.get('https://wenwen.sogou.com/cate/tag?tagId=137&ch=ww.fly.bq1', headers = headers)
res = etree.HTML(response.content)
List = res.xpath('//*[@id="categoryTabList"]/li/a/@data-tagid')
# print(List)


#请求url，并获取uuid
str_uuid =''
while 1:
    response2 = session.get('https://open.weixin.qq.com/connect/qrconnect?appid=wxcb619c36a67960d4&redirect_uri=https%3A%2F%2Fwenwen.sogou.com%2Flogin%2Fwechat%2Fsave_user_info%3Ftp%3Dwenwen_site%26business%3Dwenwen&response_type=code&scope=snsapi_login&state=3d6be0a4035d839573b04816624a415e&self_redirect=true', headers = headers)

    pattern1 = r'/connect/qrcode/([a-zA-Z0-9]+)'

    string = re.search(pattern1, response2.text).group()
    str_uuid = string.split('/connect/qrcode/')[1]

    if len(str_uuid) == 16:
        break
print(str_uuid)
# print(string)



# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
#请求url，并获取二维码
response = session.get('https://open.weixin.qq.com/connect/qrcode/'+str_uuid, headers = headers)


with open('d:/yyzm.png', 'wb') as f:
    f.write(response.content)
    f.close()

os.startfile('d:/yyzm.png')
time.sleep(10)


#请求url，并获取code
time3 = str(int(time.time() * 1000))
# while 1:
response1 = session.get('https://long.open.weixin.qq.com/connect/l/qrconnect?uuid='+str_uuid+'&last=404&_='+time3, headers = headers)
print(response1.text)
result =  response1.content.decode('utf-8')
pattern = r'window.wx_code=(.*);'

ob = re.search(pattern, result)

print(ob.group(1))
#     if ob != None:
#         if ob.group(1) == 408:
#             print('登录成功')
#             break






# 6L+Z5piv5LiA5Liq6Zeu6aKY
# 546w5Zyo5a2m5LmgUEhQ6L+Y6IO96LW25LiK5ZCXPw==




#请求有登陆状态的url
sougou = session.get('https://wenwen.sogou.com/login/wechat/save_user_info?tp=wenwen_site&business=wenwen&code='+ob.group(1)+'&state=3d6be0a4035d839573b04816624a415e', headers = headers)


# print(sougou.text[:5000])



time.sleep(5)



#请求登陆后的搜狗问问主页，并获取userId
usr_center = session.get('https://wenwen.sogou.com', headers = headers)
print(usr_center.text[:4000])
pattern1 = r"userId: '(\d+)"

res = re.search(pattern1, usr_center.text[:4000])

print(res.group(1))

#post 请求url，并提问问题
tiwen_url = 'https://wenwen.sogou.com/submit/ms/ask?_traceId=20a626e27918aeab0f14e465268f8ae6:62'

import base64
m = '想要学习hadoop怎么开始？' #要发送的问题

b = base64.b64encode(m.encode('utf-8'))
# print(data)
s = str(b)[2:-1]


headers1 = {'authority': 'wenwen.sogou.com',
'method': 'POST',
'path': '/submit/ms/ask?_traceId=6ba758954f6c076b99b9dbe00b3997f1:29',
'scheme': 'https',
'accept': 'application/json, text/javascript, */*; q=0.01',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
'content-length': '215',
'content-type': 'application/json; charset=UTF-8',
'cookie': 'SUID=3E0B17791508990A000000005C9C8EA4; SUV=1553764195738862; pgv_pvi=3722054656; IPLOC=CN1100; sct=5; sw_uuid=2178071538; ssuid=188609460; CXID=3C3B1066AF6D244B7471A83892C3924A; ad=Xyllllllll2N2mJ2lllllV1Lc6cllllltspcElllllGlllllVCxlw@@@@@@@@@@@; SNUID=C296DE5D2F2AA04B1D9D01392F183D23; ld=lZllllllll2N2DvzlllllV1TeX7llllltspcElllllUlllllpllll5@@@@@@@@@@; LSTMV=251%2C361; LCLKINT=6070; sg_uuid=4630103483; sg_uname=%E4%B8%80%E4%B8%80%E4%B8%80H; sg_upic=http%3A%2F%2Fcache.soso.com%2Fthirdwx_qlogo%2Fmmopen%2Fvi_32%2FibiakRfzxhXETSicoRaq742NZEXIDy4JoJ9ZSI4Q4CZgib35Auj06cDxNSYgV9TiaiadtOUYCnbfbTMTPl6ElusHop6A%2F132; sg_mu=1577916343; sg_lu=1467883855-b2xOTlR3Ym42M01JMkE2ZExKR0hEMndEVW83NA..; w_uin=5075740546; w_skey=olNNTwbn63MI2A6dLJGHD2wDUo74; wx_unid=olNNTwbn63MI2A6dLJGHD2wDUo74; ms_tk=1564126268679-b70094b44eac4a1e780131363227a828; qun_t1=1564126609935-8538ab6a0892879dfdaa3fc53945b176; qun_tl=1564126721046-6e1b1ddcdff22a741087a505764c9de8; qun_t0=1564126832157-ef4926576b9021866bba538491f4223d',
'origin': 'https://wenwen.sogou.com',
'referer': 'https://wenwen.sogou.com/question/ask',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
'x-requested-with': 'XMLHttpRequest',}

data = {"userId":res.group(1),"clbUid":75740546,"orig":253,"mobileSmsFlag":False,"content":"","title":s,"tags":[int(random.choice(List))],"images":[],"score":"0","anonymous":True,"seekHelpUid":None,}
dumpJsonData = json.dumps(data)
timeOut = 25
wenti_post = session.post(tiwen_url, data = dumpJsonData, headers = headers1, timeout = timeOut)

print(wenti_post.text)



# {"userId":"5075740546","clbUid":75740546,"orig":253,"mobileSmsFlag":false,"content":"","title":"UHl0aG9u55qE5YmN5pmv5aaC5L2V77yf","tags":[137,65471,94618],"images":[],"score":"0","anonymous":true,"seekHelpUid":null}


# 011SjXnS0mnPp62rWDmS0uaRnS0SjXnq

# 081MDCoO0mUZG42A0LqO0aDRoO0MDCoz


#userId: '5075707907' 0.999











# session = requests.session()

# # url = 'https://graph.qq.com/oauth2.0/login_jump'
# url1 = 'https://ssl.ptlogin2.qq.com/login'
# url2 = 'https://ssl.ptlogin2.qq.com/check'
# params1 = {'u': '2396259288',
#         'verifycode': '!DGN',
#         'pt_vcode_v1': '0',
#         'pt_verifysession_v1': '17a8170aac4c6c17559fbf9af84084581342e7d632dbbcbbd406d6b948787f140b1ba3e9e594c0ae4e3c70a23bfca2d2',
#         'p': 'Xuo5yy6H3DsiNRPniCs96G9B6yp5dk7TzOajXqna67a4JbnSca2m1Iqv48KpO20AjxvlPA-pdilEXh-7wTw7mLQzlOFYBPI9Nz9n0D272TvYGQ4v1aolLgcZhymhv5zXPsNX7tkdz6d*AoZzgMeoCBFFP4QkAN1VMQI4P8Sj62fJwv-TGR3aAA*4L*PR5dlG*Mkeq0k1TBc5fPnLDgGHYkJsepd9VMajHkiMKyy2bYV99SUIe-4czTvYx5sTW0j69bWyqhMG4WBk7XdiXDow2gYY3XtvkwEDzXDQUNQXxv3q-lybg-UKf6219pHh7RNHPBZIiqe42a9we-*MXd3aUg__',
#         'pt_randsalt': '2',
#         'u1': 'https://graph.qq.com/oauth2.0/login_jump',
#         'ptredirect': '0',
#         'h': '1',
#         't': '1',
#         'g': '1',
#         'from_ui': '1',
#         'ptlang': '2052',
#         'action': '2-10-1564040553772',
#         'js_ver': '19062020',
#         'js_type': '1',
#         'login_sig':' ',
#         'pt_uistyle': '40',
#         'aid': '716027609',
#         'daid': '383',
#         'pt_3rd_aid': '101401138',
#         'ptdrvs': 'ccDE6lgwuAZdx*Q-2J1etglqsLUnkC6N1pYQBuAjSZS--cSd6bf-F3SSaAOOofzO',}


# params2 = {'regmaster':' ',
# 'pt_tea': '2',
# 'pt_vcode': '1',
# 'uin': '2396259288',
# 'appid': '716027609',
# 'js_ver': '19062020',
# 'js_type': '1',
# 'login_sig':' ',
# 'u1': 'https://graph.qq.com/oauth2.0/login_jump',
# 'r': '0.16095882706265763',
# 'pt_uistyle': '40',}


# # response1 = session.get(url1, params = params1)

# # print(response1.text)

# response2 = session.get(url2, params = params2)

# print(response2.text)





