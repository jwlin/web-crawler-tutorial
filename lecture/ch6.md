# 6. 各類型文件的爬蟲

## 非 UTF-8 編碼的文件

* 範例程式: `ch6/non_utf.py`
* `<head>` 內的 `<meta charset="utf-8">` 指明了網頁文件所用的編碼，我們可據以解析、儲存文件資訊
* 若 `charset` 的值非 utf-8，則需配合更改程式內的編碼 e.g., `resp.encoding = 'gbk'`
    * gbk 範例: https://zhidao.baidu.com/question/48795122.html
    * big5 範例: [博客來本週 66 折](http://www.books.com.tw/activity/gold66_day/)
    * euc-jp, euc-kr...

## xml 檔案

* 範例程式: `ch6/parse_xml.py`, `ch6/example.xml`
* `findall()` 找下一層 tag; `.attrib` 取出屬性的 dict

## 補充資料: pdf 檔案

* https://imsardine.wordpress.com/2011/12/06/pdf-automation/