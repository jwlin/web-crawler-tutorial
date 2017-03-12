# 2-1. 不要重覆造輪子：寫爬蟲之前

## 寫程式之前：深呼吸，再想想是否有其他方法

先搜尋 "爬蟲", 下載", "Crawler", "Downloader" 等你認為適合的關鍵字, 搞不好已經有人做好了：

* 現成的服務 (e.g., [Keepvid](http://keepvid.com/), 券商 App, 財報狗)
* 打包好的資料 (e.g., [維基百科](https://zh.wikipedia.org/wiki/Wikipedia:%E6%95%B0%E6%8D%AE%E5%BA%93%E4%B8%8B%E8%BD%BD))
* 寫好的程式 (e.g., [ComicCrawler](https://github.com/eight04/ComicCrawler))

## 非寫程式不可時：考慮以下順序

* API (imdb, Facebook, Youtube, Twitter, ...)
* URL 或網址連結是否有規則 (日期, 代號, ...)
* JavaScript, Json
    * http://www.tpex.org.tw/web/stock/aftertrading/daily_trading_info/st43.php?l=zh-tw
* 網頁很複雜時，試試"列印此網頁"或行動版網頁

## 小結："直接開始爬網頁"永遠是最後一個選項

# 2-2. BeautifulSoup 講解與網頁結構巡覽

## 2-2-1. `find_all()`, `find()`, `.text`, `stripped_strings`

* [範例網頁](http://blog.castman.net/web-crawler-tutorial/ch2/blog/blog.html)
* 定位元件
    * `find()` 回傳第一個找到的元件; `find_all()` 回傳所有元件
    * `find_all(tag_name, tag_attrs, ..., **kwargs)`
    * 95% 的時間只會用到 tag, attribute (class, id, name, 其他特殊屬性)與 key=value
* 取得文字
    * `.text (get_text())` (包含以下所有階層)
    * `stripped-strings`: 回傳 iterator object, 需巡覽以取出其中的值
* 補充資料
    * https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
    * https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text
    * https://www.crummy.com/software/BeautifulSoup/bs4/doc/#strings-and-stripped-strings

## 2-2-2. 網頁結構巡覽

* [範例網頁](http://blog.castman.net/web-crawler-tutorial/ch2/table/table.html)

```
body
  - div
    - h2
    - p
    - table.table
      - thead
        - tr
          - th
          - th
          - th
          - th
      - tbody
        - tr
          - td
          - td
          - td
          - td
            - a
              - img
        - tr
        - ...
        
```

* 雖然 `find()`, `find_all()` 可以處理大部分問題, 但有時候巡覽網頁結構 (parent, children, next and previous siblings) 比較好用
* 補充資料 
    * https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree

# 2-3. 正規表示式 (regular expression)

* 簡潔表示字串規則的方式
* [線上測試 regex](http://www.regexpal.com/)

```
這系列文章是給初學者的網頁爬蟲與資料分析教學，如果你對於 Python 有粗淺認識 (知道 Python 的資料型態, 控制結構, 寫過一些小程式), 想進一步知道要怎麼使用 Python 擷取網頁資訊並簡單做些資料分析 (如圖表、統計資料、相關性等)，這系列文章可以帶你入門。

一般想要寫網頁爬蟲的人，不會只想要擷取資料，他們真正想要的通常是資料分析，找出資料能提供的資訊，或使用資料驗證自己的假設，Python 也有許多資料處理與展示的好用套件可以使用 (如 NumPy, scikit-learn, pandas)，這系列文章會先略過這些套件，教你直接用程式計算統計資料與畫圖，以便讓你更了解套件底層的邏輯，之後學習這些套件時會更容易上手。 

聯絡我們 pycone2016@gmail.com
http://www.pycone.com
```

* 常見的 rule
    * Email:	`[A-Za-z0-9\._+]+@[A-Za-z0-9\._]+\.(com|org|edu|net)`
    * URL:	`http(s)?://[A-Za-z0-9\./_]+`
    * 所有中文字(不含標點符號): `[\u4e00-\u9fa5]+`
    * [Unicode 查詢](http://unicodelookup.com). e.g., 標點符號
    * **Google!** e.g., "email regex", "phone regex", "中文字 regex", ...
* 補充資料
    * https://docs.python.org/3.5/library/re.html
    * https://atedev.wordpress.com/2007/11/23/%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%A4%BA%E5%BC%8F-regular-expression/
