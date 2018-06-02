# 8. 處理表單及登入頁

* HTTP Method: GET 與 POST
* 從 Chrome 開發者工具 >> Network  看到 HTTP Method, 以及 POST 送出的表單資料 (Form Data)
* (若要完全模仿瀏覽器, 則需再考慮 Header, Cookie, etc.)

## 範例: 台灣證券交易所股票資料

### 2017/05/27: 該網頁已經更新，改用 GET JSON 的方式。同學 yotsuba1022 提供了對應的範例程式[請點此](https://github.com/yotsuba1022/web-crawler-practice/blob/master/ch4/tw_stock_exchange.py) 或看 `ch8/twse.py`

* 範例: `ch8/trading_post.py`
* http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAYMAIN.php

```
data = {
  'query_year': year,
  'query_month': month,
  'CO_ID': stock_id,
}
requests.post(URL, data=data)
```

## 範例: 空氣品質監測網

### 2018/06/02: 網頁網址改為 HTTPS 及 form data 微幅更新。已修正程式碼。
### 2017/05/28: 該網頁已經更新，請將 POST 到 Server 的 Key 從 `ctl08$...` 改為 `ctl09$...`

* 範例: `ch8/taqm_epa.py`
* http://taqm.epa.gov.tw/taqm/tw/HourlyData.aspx
* ASP.NET 網頁的安全機制 (類似 [CSRF 機制](https://zh.wikipedia.org/wiki/%E8%B7%A8%E7%AB%99%E8%AF%B7%E6%B1%82%E4%BC%AA%E9%80%A0) ): 除了查詢必須的表單資料以外, 還要額外送出`__VIEWSTATE`, `__VIEWSTATEGENERATOR`, `__EVENTVALIDATION `

## 補充資料: [Postman 工具](https://www.getpostman.com/docs/introduction)
