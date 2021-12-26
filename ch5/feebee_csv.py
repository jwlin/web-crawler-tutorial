import requests
import urllib.parse
import csv
import re
from bs4 import BeautifulSoup


if __name__ == '__main__':
    query = 'ps5主機'
    q = urllib.parse.quote(query)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.181 Safari/537.36'}
    # e.g. https://feebee.com.tw/s/?q=ps5%E4%B8%BB%E6%A9%9F    
    page = requests.get("https://feebee.com.tw/s/?q=" + q, headers=headers).text
    soup = BeautifulSoup(page, 'html5lib')
    items = list()
    for link in soup.find_all('span', 'items_container'):
        item = [
            link.a.attrs["title"],
            link.a.attrs["data-price"],
            link.a.attrs["data-store"]
        ]
        items.append(item)
    print('共 %d 項商品' % (len(items)))
    for item in items:
        print(item)

    # 讓 Excel 開啟不會亂碼的方式
    # 1.
    # with open('feebee.csv', 'wb') as f:
    #     f.write(b'\xEF\xBB\xBF')  # 在檔頭加上 UTF-8 編碼的 BOM
    # with open('feebee.csv', 'a', encoding='utf-8', newline='') as f:
    #
    # 2.
    # with open('feebee.csv', 'w', encoding='utf-8-sig', newline='') as f:

    with open('feebee.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(('品項', '價格', '商家'))
        for item in items:
            writer.writerow((column for column in item))
    '''
    print('讀取 csv 檔')
    with open('feebee.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['品項'], row['價格'], row['商家'])
    '''
