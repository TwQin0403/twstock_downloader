# -*- coding: utf-8 -*-
'''
The interface of twstock_downloader
'''
from . import fetch
from . import utils
from io import FileIO
import json
from pathlib import Path
import os

def get(filepath=None):
    '''
    if the script couldn't find the target file would automatically download the all historical data  
    '''
    if filepath is None:
        print("Don't Provide the filepath")
        filepath = os.getcwd()
        filepath = Path(filepath) / Path('result.json')
        print('Generate the filepath {}'.format(filepath))

    try:
        data = json.load(FileIO(Path(filepath),'r'))
        url_list = utils.get_url_list(data['current'])
        get_by_url_list(url_list,filepath)

    except:
        print("Cannot find the existing file")
        print("Fetch all data")
        data = {}
        with open(filepath,'w',encoding='utf-8') as f:
            json.dump(data,f)
        start = '2004-02-11'
        url_list = utils.get_url_list(start)
        get_by_url_list(url_list,filepath)
                
def get_by_url_list(url_list,filepath):
    print('Total days {} to fetch'.format(len(url_list)))
    chunks = [url_list[x:x+50] for x in range(0, len(url_list), 50)]
    print('Split into chunks {}'.format(len(chunks)))
    for chunk in chunks:
        data = fetch.fetch_by_url_list(chunk)
        old_data = json.load(FileIO(Path(filepath),'r'))
        old_data.update(data)
        with open(filepath,'w',encoding='utf-8') as f:
            json.dump(old_data,f)

if __name__ == '__main__':
    get()