import requests
from bs4 import BeautifulSoup


def baidu_test():
    resp = requests.get('https://zhidao.baidu.com/question/48795122.html')
    resp.encoding = 'gbk'  # 該網頁為 gbk 編碼
    soup = BeautifulSoup(resp.text, 'html.parser')
    title = soup.find('span', 'ask-title').text.strip()
    content = soup.find('span', 'con').text.strip().replace('\n', '')
    print('title:', title)
    print('content:', content)
    try:
        with open(title + '.txt', 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(e)


def gold_66_test():  # 20190120: 博客來 66 折網址已換，且改為 utf-8 編碼，此函式已失效
    resp = requests.get('http://www.books.com.tw/activity/gold66_day/')
    resp.encoding = 'big5'  # 該網頁為 big5 編碼
    soup = BeautifulSoup(resp.text, 'html.parser')
    books = list()
    for div in soup.find_all('div', 'sec_day'):
        books.append(div.h1.a.text + div.find_all('h2')[1].text + div.find_all('h2')[2].text)
    print('\n'.join(books))
    try:
        with open('66.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(books))
    except Exception as e:
        print(e)


def gold_66_new():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.181 Safari/537.36'}

    # 今日 66 折的資料已改由 AJAX 方式從以下網址取回
    resp = requests.get("https://activity.books.com.tw/crosscat/ajaxinfo/getBooks66OfTheDayAjax/P?uniqueID=E180629000000001_94", headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    print('今日 66 折:', soup.h1.text)
    ul_price = soup.find('ul', 'price clearfix')
    print(list(ul_price.stripped_strings))

    print('每日一書66折預告')    
    resp = requests.get('https://activity.books.com.tw/crosscat/show/books66', headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    div_next_66 = soup.find('div', 'mod-04 clearfix')    
    for d in div_next_66.find_all('div', 'table-td'):
        print([s for s in d.stripped_strings])


if __name__ == '__main__':
    baidu_test()
    # gold_66_test()
    gold_66_new()
