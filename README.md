twstock_downloader
========================
從台灣證交所下載每日股票價個的簡單套件。


## 安裝(installation)
```
pip install twstock_downloader
```

## Quick Start

```python
import twstock_downloader

twstock_downloader.get()
```

## usage

這邊套件只接受一個引數(filepath)

```python
twstock_downloader.get(filepath='C:\Users\Qin\workspace\twstock_downloader\twstock_downloader\result.json')
```
指定檔案存取的位置，沒有給定便會存在執行程式所待的資料夾，並從2004-02-11開始抓取(證交所的最早紀錄)

如果檔案已經存在，則會讀取檔案，取得檔案目前抓到的日期，從那天開始更新。



#### How to load the data
檔案的格式會長成表的中文名對應表格的json結構，可用下列程式還原為表名:pandas.DataFrame的字典結構

```python
with open('download_TWCB.json','r',encoding='utf-8') as f:
    test_data = json.load(f)

test_data.pop('current'.None)
test_data = {key:pd.read_json(test_data[key]) for key in test_data.keys()} 
```