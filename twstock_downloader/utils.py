# -*- coding: utf-8 -*-
import datetime

def trans_date(date_time):
    return ''.join(str(date_time).split(' ')[0].split('-')) 

def get_url(date_time):
    url = 'http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + date_time +'&type=ALLBUT0999'
    return url

def get_date(url):
    date_time = url.split("&")[1].split("&")[0].replace('date=','')
    return date_time

def get_url_list(start):
    try:
        start = datetime.datetime.strptime(start,'%Y-%m-%d')
    except:
        start = datetime.datetime.strptime(start,'%Y%m%d')
    now_date = datetime.datetime.now()
    days = (now_date - start).days
    date_time_list = [start + datetime.timedelta(days=day+1) for day in range(days)]
    date_time_list = [get_url(trans_date(date)) for date in date_time_list]
    return date_time_list

    