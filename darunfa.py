import requests
import json
import time
from playsound import playsound
print('开始获取购物车信息...')
while True:
    url = 'http://yx.feiniu.com/cart-yxapp/shopcart/adminshopcart/cartget/t141'

    headers={
        'Host': 'yx.feiniu.com',
        'Connection': 'keep-alive',
        'Content-Length':'790',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'content-type':'application/x-www-form-urlencoded',
        'Referer':'https://servicewechat.com/wx08cc6bd15fabfa53/84/page-frame.html',
        'Accept-Encoding':'gzip, deflate, br',
    }

    data={"data":'{"apiVersion":"t141","appVersion":"1.5.1","areaCode":"CS000016","channel":"online","clientid":"*********027035","device_id":"***********kiTz","time":1649468558204,"reRule":"4","token":"*************a8f140","viewSize":"720x1184","networkType":"wifi","isSimulator":false,"osType":"4","scopeType":1,"businessType":1,"businessId":"11020001","deliveryCircleType":"1","body":{"ticket_id":"","store_id":"1102","notNeedScallion":""}}',
        "h5":"yx_touch",
        "paramsMD5":"RWMk/1EAEzT2qlzrKz67LJ7aWqHqCBu7JQ/UwJR7v8Q=",
    }
    r=requests.post(url,json=data,data=data,headers=headers)
    result=r.json()
    newresult=result['body']['settlementDesc']
    newresultj=result['body']['canSettlement']
    print('库存:'+newresult)
    if newresultj == True:
        song = 'warn.mp3'
        playsound(song)
    if newresultj == False:
        time.sleep(0.25)
