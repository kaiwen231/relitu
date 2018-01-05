#coding=utf-8
from urllib import quote,urlopen
import json
import csv
def getlnglat(address):
    url='http://api.map.baidu.com/geocoder/v2/'
    output='json'
    ak='lpGGISoRxTQEqhk3I0t9ysrt9q7M6XGr'
    address=quote(address)
    uri=url + '?address=' + address + '&output=' + output + '&ak=' + ak
    rep=urlopen(uri)
    res=rep.read()
    temp=json.loads(res)
    return temp

file=open('point.json','w')
with open(r'C:\Users\kevin\git-project\relitu.csv','r') as csvfile:
#csvfile=open(r'各地区住宅商品房平均销售价格.csv','r')
    csv_reader=csv.reader(csvfile)
    for line in csv_reader:
        if csv_reader.line_num==1:
            continue
        address=line[0]
        price=line[1]
        lng=getlnglat(address)['result']['location']['lng']
        lat=getlnglat(address)['result']['location']['lat']
        str_json='{"lng":' + str(lng) + ',"lat":' + str(lat) + ',"count":' + str(price) + '},'
        file.write(str_json)
file.close()

