#!/usr/bin/python
#-*-coding: utf-8 -*-

from lxml import html
from urllib.request import urlopen
import re
import requests
from bs4 import BeautifulSoup
from urllib import request
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='projectone')
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=None, db='mysql')

def trade_spider(max_pages):
    page = 0
    while page <= max_pages:
        #url = 'http://www.ocpb.go.th/more_news.php?offset=0&cid=24&filename=index'
        url = "http://www.ocpb.go.th/more_news.php?offset=" + str(page) + "+&cid=24&filename=index"
        html_ = urlopen(url).read()
        unicode_str = html_.decode("cp874")
        encoded_str = unicode_str.encode("utf8")
        tree = html.fromstring(unicode_str) #เก็บค่าเอาไว้ในรูปแบบ html


        q = tree.xpath("//span[@class='text_head']/text()") #เติม text() เข้าไปเพื่อดึงข้อความ
        #q = tree.xpath("//a[@class='text_head']/text()")
        count = 0
        for c in q:
            count+=1

            if count%2!=0:
                a=c.encode("utf8")
                #print(a)
            else :
                b=c.encode("utf8")
                #print(b)
        cursor = conn.cursor()
        cursor.execute('''INSERT into ocpb(company_name,project_name)
                        values (%s,%s)''',
                        (a,b))
        conn.commit()
        cursor.close()

        page +=1

trade_spider(11000)