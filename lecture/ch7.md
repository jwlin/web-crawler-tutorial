# 7. 實務專題: 手機比價程式

## 比價標的

```
2022/01/05 更新: 配合現況，程式碼改為搜尋 iPhone 13 Pro 的價錢
```
* iPhone 7 Plus 128G

## 比價來源

### momo 購物網 (行動版網頁)

```
2020/07/19 更新: 網站已改版，更新程式碼
```

* 此網站已經改成使用 AJAX 動態更新正確的價格資訊，所以程式所抓到的價格資訊會是折扣前的原價。如要取得網頁上看到的折扣後價格，可考慮使用 WebDriver, 或是觀察其 AJAX 執行邏輯 (透過什麼網址及參數，取得商品折價資料，如下圖所示)

<img src="https://i.imgur.com/gB7IYCw.jpg" width="450"/>

```
2019/09/28 更新:  小幅更新程式碼以取得商品照片
```

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
