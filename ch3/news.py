import requests
from bs4 import BeautifulSoup


def main():
    print('蘋果今日焦點')
    dom = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/headline').text
    soup = BeautifulSoup(dom, 'html5lib')
    for ele in soup.find('ul', 'all').find_all('li'):
        print(
            ele.find('div', 'aht_title_num').text,
            ele.find('div', 'aht_title').text,
            ele.find('div', 'aht_pv_num').text
        )
    print('-----------')
    print('自由今日焦點')
    dom = requests.get('http://news.ltn.com.tw/list/newspaper').text
    soup = BeautifulSoup(dom, 'html5lib')
    for ele in soup.find('ul', 'list').find_all('li'):
        if ele.find('a', 'tit'):
            print(ele.find('a', 'tit').text.strip())

if __name__ == '__main__':
    main()
