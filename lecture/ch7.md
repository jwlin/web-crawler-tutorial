# 7. 實務專題: 手機比價程式

## 比價標的

* iPhone 7 Plus 128G

## 比價來源

### momo 購物網 (行動版網頁)

***20190928 更新:  小幅更新程式碼以取得商品照片***

* 網址格式: http://m.momoshop.com.tw/mosearch/[YOUR_QUERY].html
* requests 必須附上 `User-Agent` header

```
headers = {'User-Agent': 'mozilla/5.0 (Linux; Android 6.0.1; '
                         'Nexus 5x build/mtc19t applewebkit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2702.81 Mobile Safari/537.36'}
resp = requests.get(url, headers=headers)
```

* 範例程式: `ch7/search_momo.py`

### PChome 24h 購物 (API)

* API 格式: http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=[YOUR_QUERY]
* 範例程式: `ch7/search_pchome.py`

### 資料顯示

* 兩家賣場該手機的每日均價走勢
* 讀取`json` 目錄下所有的 json 檔案, 將兩家賣場每日的資料分別取出
* 範例程式: `ch7/show_stat.py`