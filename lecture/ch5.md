# 5-1. 資料儲存：圖片與多媒體檔案

## 儲存連結 (e.g, URL) 或實體檔案？考量點：

* 節省程式運作時間；節省儲存空間；程式複雜度低 (不須處理檔案下載或檔名亂碼等)
* 連結失效；不想耗用他站資源

## 爬蟲實戰五：PTT 表特版圖片下載器

* 範例程式: `ch5/ptt_beauty.py`
* 下載圖片: `urllib.request.urlretrieve(url, file_name)`

### 流程

1. 取得今日所有文章的超連結 (詳細作法可參考單元 3-1)
2. 連結到文章內容, 在裡面尋找圖片網址 (imgur.com)
3. 使用文章標題作為資料夾名稱，下載圖片

### 文字處理注意事項

* 用正規表示式擷取合法網址們
```
http://i.imgur.com/A2wmlqW.jpg,
http://i.imgur.com/A2wmlqW  # 沒有 .jpg
https://i.imgur.com/A2wmlqW.jpg
http://imgur.com/A2wmlqW.jpg
https://imgur.com/A2wmlqW.jpg
https://imgur.com/A2wmlqW
http://m.imgur.com/A2wmlqW.jpg
https://m.imgur.com/A2wmlqW.jpg
```
* 下載圖片時用的網址必須是 i.imgur.com 開頭, 且為 .jpg 結尾
* 因為文章標題可能會有作業系統不支援的字元，所以要處理創造目錄 (`os.makedirs()`) 時發生的例外

# 5-2. 資料儲存：CSV 檔 (爬蟲實戰六：ezprice)

* ezprice 的比價網址: https://ezprice.com.tw/s/[QUERY]/price/
* [QUERY] 可以是中文或多個字: 用`urllib.parse.quote()`做 HTML Encoding
* 用 `csv` 模組寫入 csv 檔 (記得 `encoding='utf-8', newline=''` 參數)
* `csv.DictReader()` 讀取第一列為標題的 csv 檔
* Windows 用 excel 開啟 csv 檔是亂碼如何解決? 資料->從文字檔 匯入

# 5-3. 資料儲存：資料庫 (SQLite)

* 關聯式資料庫 (Relational Database): 如同一張張的表格, 每張表格有不同欄位
* 使用資料庫的好處: 加快查詢速度 (建立索引), 進階查詢功能, 多執行緒或平行讀寫等
* SQLite: 小而全, 小而美, 支援 SQL 標準語法, 零安裝, Python 直接內建支援, 處理 TB 規模的資料, 支援每日百萬次瀏覽的網站沒有問題
* GUI: http://sqlitebrowser.org/
* 語法查詢 (建議直接 Google 最快): http://www.1keydata.com/tw/sql/sqlselect.html