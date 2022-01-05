# 9. 處理動態網頁 (Selenium Webdriver)

```
2022/01/05 更新: 更新台銀法拍屋網址及 WebDriver 下載網址
```

* 範例: `ch9/bot_house.py`
* 與其模仿瀏覽器，不如直接使用瀏覽器
    * 優點: 能夠解決大部分的障礙
    * 缺點: 執行速度, 例外處理...
* 前置作業
    * 安裝 selenium library (已經包含在 requirements.txt 中)
    * 下載 [Chrome Webdriver 執行檔](https://sites.google.com/chromium.org/driver/), 解壓縮後放在專案目錄下
* Webdriver 可以做的事:
    * 定位網頁元件 (find_element_by_id/tag/name/class...)
    * 點擊, 輸入文字, 選擇選單, 拖拉...
    * 下載目前看到的網頁原始碼 (後續使用 Beautifulsoup 解析並取得資訊)
* 範例: https://www2.bot.com.tw/house/default.aspx
(第一次啟動 webdriver 時, Windows 會跳出防火牆警告, 請准許)
* 補充資料: Webdriver 的執行檔也可以使用 [PhantomJS](http://phantomjs.org/download.html), 可以在背景模仿瀏覽器行為, 或可加快程式執行速度
* 2018/06/23 補充：現在可以使用 headless 的 Chrome, 讓 Chrome 瀏覽器在背景執行，不需要另外下載執行 PhantomJS, 範例程式碼如下：

```
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options, executable_path='[chromedriver.exe 所在位置]')
```
