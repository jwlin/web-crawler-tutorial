# 3-1. 爬蟲實戰一：PTT 八卦版今日熱門文章

* 範例: `ch3/ptt_gossiping.py`
* https://www.ptt.cc/bbs/Gossiping/index.html
* "看板內容需滿十八歲方可瀏覽": `set-cookie: over18=1;`
* 所需文章資料:
    * 每一篇文章: \<div class="r-ent"\>
    * 標題: \<a\> text
    * 網址: \<a href=\>
    * 推文數: \<div class="nrec"\>
    * 日期: \<div class="date"\>
    * 上一頁按鈕所在: \<div class="btn-group btn-group-paging"\>

## 流程

1. 從最新頁面進入
2. 取得此頁所有今日文章與上一頁的超連結
3. 若此頁包含今日文章, 則暫存起來之後, 連到上一頁, 進行步驟 2
4. 顯示熱門文章 / 儲存所有文章...等各種處理

## 作業: PTT 八卦版今天有多少不同的 5566 id 發文
![](https://i.imgur.com/pE8y1c7.png)

### 提示

1. 文章作者資訊被什麼 tag 包圍
2. 如何判斷不同的 5566 id
3. 解答在範例程式中, 搜尋 `author` 以及 `get_author_ids`

# 3-2. 爬蟲實戰二：Yahoo 奇摩電影本週新片

## 2017/08/27 更新: 該網頁結構有變，已更新程式碼為正確版本

* 範例: `ch3/yahoo_movie.py`
* https://tw.movies.yahoo.com/movie_thisweek.html
* 觀察各項資訊所在的 tag 及網址
    * 電影資訊所在區塊: `soup.find_all('div', 'release_info_text')`
    * 期待度: `row.find('div', 'leveltext').span.text`
    * 中文名: `row.find('div', 'release_movie_name').a.text`
    * 上映日: `row.find('div', 'release_movie_time').text`
    * 簡介: `row.find('div', 'release_text')`
    * 預告片網址: `row.find_next_sibling('div', 'release_btn color_btnbox').find_all('a')[1]`
    * ...
* 如何取得電影 id 以及完整電影海報網址

## 作業: 取得每部電影的全文介紹

### 提示

1. 電影詳細資訊在 https://tw.movies.yahoo.com/movieinfo_main.html/id=MOVIE_ID
2. 觀察電影全文介紹內容被什麼 tag 包圍
3. 解答在範例程式的 `get_complete_intro()`

# 3-3. 爬蟲實戰三：兩大報今日焦點新聞

## 2018/02/15 更新: 兩大報網頁結構有微幅變動，已更新程式碼為正確版本

* 範例: `ch3/news.py`
* 蘋果今日焦點: http://www.appledaily.com.tw/appledaily/hotdaily/headline
    * 進入點: `<ul class="focus">` \> `<li>`
* 自由今日焦點: http://news.ltn.com.tw/list/newspaper
    * 進入點: `<ul class='list'>` \> `<li class='tit'>`

# 3-4. 爬蟲實戰四：Google Finance 網頁

* 範例: `ch3/google_finance.py`
* https://www.google.com/finance?q=MARKET:STOCK_ID
* 個股資訊分布在 \<div id="price-panel"\> 與 \<div class="snap-panel"\> 兩個區塊中

## 作業: 取得個股的歷史資料

### 提示:

1. 個股歷史資料網址: https://www.google.com/finance/historical?q=MARKET:STOCK
2. 全部的資料都在 \<table\> 內
3. 參考作法在範例的 `get_stock_history()` 內
4. 小挑戰: 如何取得下一頁/不同日期的歷史資料? 提示: 觀察網址的參數


# 第三章作業: Yahoo 奇摩字典

## 提示

1. 網址: https://tw.dictionary.yahoo.com/dictionary?p=QUERY
2. **[重要]** `requests.get()` 取得的網頁文件與開發者工具/檢視原始碼看到的文件不同? 請在 header 加上 Referer
```
requests.get(
    'https://tw.dictionary.yahoo.com/dictionary?p=' + QUERY,
    headers={'Referer': 'https://tw.dictionary.yahoo.com/dictionary?'}
)
```
3. 先嘗試單字的 QUERY
4. 但 QUERY 也可以是中文或多個英文字, e.g.,
* "good at": `https://tw.dictionary.yahoo.com/dictionary?p=good+at`
* "傳統": `https://tw.dictionary.yahoo.com/dictionary?p=%E5%82%B3%E7%B5%B1`
* 如何取得 QUERY 的 URL Encoding? `urllib.parse.quote_plus()`
* 參考作法: `ch3/yahoo_dict.py`
