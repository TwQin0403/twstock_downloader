twstock_downloader
========================
從台灣證交所下載每日股票價格的簡單套件。


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
存出來的檔案是一個json檔案，基本上為日期對應每日的股價的資料格式，可用下面的程式碼還原為日期(字串)對應pandas.DataFrame的格式

```python
with open('result.json','r',encoding='utf-8') as f:
    test_data = json.load(f)

test_data.pop('current', None)
test_data = {key:pd.read_json(test_data[key]) for key in test_data.keys()} 
```

其中，current這個key是用來告訴程式要從那邊開始抓起，如果不想從2004-02-11開始抓取，可以先產生一個空的json的檔案，裡面為{'current':'想要的日期(例如:20200811)'}
