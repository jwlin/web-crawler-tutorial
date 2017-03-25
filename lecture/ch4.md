# 4-1. 網站 API 簡介

## API = 網站規定好，(透過程式)跟它要資料的方式

* 該網站希望你跟它要資料的方法/規則，通常比直接爬網頁方便
* 方便該網站控管資料流量/使用者驗證 (API key/token...)
* 與網站溝通的方法 (HTTP Methods):
    * GET: 直接貼上網址(及參數)就能**取得**資料 ("GET me the infomation")
    * POST: 在背景**送出**我的資料，希望 Server 能夠處理 ("SUBMIT data to the server") 
    * PUT: 在背景送出我想**更新**的資料 ("UPDATE the record in the DB")
    * DELETE: 在背景送出我想**刪除**的資料 ("REMOVE the record in the DB")

## 網站的回應格式

* JSON (e.g., http://www.omdbapi.com/?t=iron+man)
* XML (e.g., http://www.omdbapi.com/?t=iron+man&r=xml)
* 安裝瀏覽器插件 ("JSON/XML Formatter") 或線上轉換可方便觀察資料
    * Chrome 插件: [JSON](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en)/[XML](https://chrome.google.com/webstore/detail/xml-tree/gbammbheopgpmaagmckhpjbfgdfkpadb?hl=en)
    * 線上轉換: [JSON](http://jsonparseronline.com/)/[XML](http://codebeautify.org/xmlviewer)

## API 常見格式

https://popularblog.com/api/v4/json/users/1234/posts?api_key=YOUR_API_KEY&from=08012016?to=12310216&format=json


# 4-2. 網站 API 實戰一：PTT 八卦板眾來源國家分布

* 範例: `ch4/ptt_gossiping_ip.py`

## http://freegeoip.net

* 免費查詢網址或 IP 的地理資訊
* 支援 JSON/XML/CSV 回傳格式
* 每小時 15000 次查詢額度
* http://freegeoip.net/json/hahow.in (或 http://freegeoip.net/json/104.155.210.11)

```
{
  "ip": "104.155.210.11",
  "country_code": "US",
  "country_name": "United States",
  "region_code": "CA",
  "region_name": "California",
  "city": "Mountain View",
  "zip_code": "94043",
  "time_zone": "America/Los_Angeles",
  "latitude": 37.4192,
  "longitude": -122.0574,
  "metro_code": 807
}
```

## 流程

1. 取得今日所有文章的超連結 (詳細作法可參考單元 3-1)
2. 連結到文章內容, 在裡面尋找發文者 ip
3. 使用 freegeoip.net API 查詢 ip 來源國家
4. 顯示來源國家分布
 
# 4-3. 網站 API 實戰二：Facebook Graph API
 
# 4-4. 網站 API 實戰三：imdb

* 範例: `ch4/imdb.py`
* 非官方 API: www.omdbapi.com
    * Search by title/ID
    * Search by keywords (若結果超過 10 筆, 如何換頁?)
    * 中文電影: 先確認英文名字或 imdb id
* 找出所有 "iron man" 相關影片及相關統計資料 (類型分布, 平均評價)
    1. 用 keywords 搜尋所有相關影片, 記錄其 movie id 
    2. 用 id 搜尋所有影片, 紀錄
    3. 顯示結果
* Python 套件: https://github.com/dgilland/omdb.py

 
# 4-5. 網站 API 實戰四：Google Finance API

* 範例: `ch4/google_finance_api.py`
* 官方已經[取消支援](https://developers.google.com/finance/) Google Finance API
* 即時股價 e.g., http://finance.google.com/finance/info?client=ig&q=TPE:2330
    * q: 證交所:股票代碼 (e.g., TPE:2330, NASDAQ:GOOG)
    * 回傳資料欄位不多, 可參考對照網頁版 (e.g., https://www.google.com/finance?q=TPE:2330)
* 歷史股價 e.g., http://www.google.com/finance/getprices?q=2330&x=TPE&i=86400&p=3d
    * q: 股票代號或代碼 (e.g., 2330, GOOG)
    * x: 證交所代碼 (e.g., TPE, NASDAQ)
    * i: 每一列數值的時間間隔(秒) (e.g., 86400=以天為單位, 3600=以小時為單位)
    * p: 資料時間 (e.g, 1d=1天, 1M=1個月, 1Y=1年)
    * 回傳資料
        * 第一列的時間是 Unix Timestamp (從 1970/1/1 開始至今的秒數), 可用 `datetime.datetime.fromtimestamp()` 轉換為可讀日期
        * 接著每一列的第一個數字是經過的時間間隔數
        * 其餘欄位定義與歷史資料網頁相同 (e.g., https://www.google.com/finance/historical?q=TPE%3A2330)
* 補充資料:
    * [Google Finance](https://www.google.com/googlefinance/disclaimer/) 的證交所代號列表, 更新時間, 免責聲明
    * 使用 Yahoo/Google API 取得歷史股價資料的 [blog 文章](http://lovecoding.logdown.com/posts/257928-use-yahoo-api-to-obtain-historical-stock-price-data)