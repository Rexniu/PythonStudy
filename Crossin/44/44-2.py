#-*- coding:utf-8 -*-
import urllib2
import json
from city import city

cityname = raw_input('你想查询那个城市的天气？\n')
citycode = city.get(cityname)
print citycode
if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' %citycode)
    content = urllib2.urlopen(url).read()
    print content
