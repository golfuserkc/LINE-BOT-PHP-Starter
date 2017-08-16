#!/usr/bin/python
#-*-coding: utf-8 -*-
# import requests
#
# proxies = {'http': 'socks5://127.0.0.1:9150',
#            'https': 'socks5://127.0.0.1:9150'}
#
# resp = requests.get('http://proxy.fpo.go.th/FPO/modules/Petition/update_count_visit.php?mod=Petition&categoryID=CAT0000079&petitionID=1178&file=answer&visit_count=1', proxies=proxies)
#
# print(resp.text)
# class BrickSetSpider(scrapy.Spider):
#     name = "brickset_spider"
#     start_urls = ['http://brickset.com/sets/year-2016']
#     print(start_urls)

from urllib.request import Request, urlopen
import re
from lxml import html
from urllib.request import urlopen
import re
import requests
from bs4 import BeautifulSoup
from urllib import request
import pymysql
req = Request('http://www.fpo.go.th/FPO/index2.php?mod=Petition&categoryID=CAT0000079&petitionID=1069&file=answer', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
unicode_str = webpage.decode("utf8")
tree = html.fromstring(unicode_str) #เก็บค่าเอาไว้ในรูปแบบ html
q = tree.xpath("//span[@class='text_head']/text()")


print(unicode_str)

