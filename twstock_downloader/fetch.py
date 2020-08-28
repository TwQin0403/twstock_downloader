# -*- coding: utf-8 -*-
import pandas as pd
import requests
import io
import time
import logging
import random
import pdb
from . import  utils

def fetch_by_url(url):
    time.sleep(5)
    page = requests.get(url)
    use_text = page.text.splitlines()
    for i,text in enumerate(use_text):
        if text == '"證券代號","證券名稱","成交股數","成交筆數","成交金額","開盤價","最高價","最低價","收盤價","漲跌(+/-)","漲跌價差","最後揭示買價","最後揭示買量","最後揭示賣價","最後揭示賣量","本益比",':
            initial_point = i
            break
    df = pd.read_csv(io.StringIO(''.join([text[:-1] + '\n' for text in use_text[initial_point:]])))
    df['證券代號'] = df['證券代號'].apply(lambda x:x.replace('"',''))
    df['證券代號'] = df['證券代號'].apply(lambda x: x.replace('=',''))
    return df


def fetch_by_url_list(url_list,verbose=False):
    df_dict = {}
    print("The number of days is {}".format(len(url_list)))
    for i,url in enumerate(url_list):
        print("Start to process the {}/{}".format(i+1,len(url_list)))
        try:
            df = fetch_by_url(url)
            df_json = df.to_json()
            date = utils.get_date(url)
            df_dict.update({date:df_json})
            df_dict.update({'current':utils.get_date(url)})
            if verbose:
                print("Succeed at " + date)
        except:
            if verbose:
                print('Fails at ' + utils.get_date(url))
            pass
    return df_dict    