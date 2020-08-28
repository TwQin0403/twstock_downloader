# -*- coding: utf-8 -*-
from .context import twstock_downloader

class TestFetch:
    """Basic test cases."""
    
    def test_fetch_single_sheet(self):
        urls = ['https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20040211&type=ALLBUT0999',
                'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20200817&type=ALLBUT0999',
                'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20200828&type=ALLBUT0999']
        for url in urls:
            print(twstock_downloader.fetch.fetch_by_url(url).head())