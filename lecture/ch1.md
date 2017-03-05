# https://github.com/jwlin/web-crawler-tutorial

# 1-1 環境設定與套件安裝

* Python3 與 pip
* virtualenv 的好處: 隔離專案環境, 打包容易
* virtualenv cmd 的基本使用方式
```buildoutcfg
pip install virtualenv
virtualenv [ENV_DIR]
# 啟動 virturalenv (隔離環境)
[ENV_DIR]/Scripts/activate
# 結束 virturalenv (回到 global 環境)
deactivate
```
* PyCharm 的好處, 基本設定, 在 PyCharm 內設定 virtualenv

# 1-2 網頁爬蟲初探與例外狀況處理

* 網頁 = 由標籤 (tag) 所組成的階層式文件
* HTML (網頁的骨架結構)、CSS (網頁的樣式) 與 JavaScript (在瀏覽器端執行，負責與使用者互動的程式功能)。
* 用 `find()` 找標籤, `.text` 取文字
* 網路世界是雜亂的，永遠要記得處理例外，避免爬蟲中斷
  * 網站連不上
  * 找不到網頁
  * 找不到 Tag 或 Tag 的屬性