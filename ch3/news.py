import requests
from bs4 import BeautifulSoup


def main():
    print('蘋果今日熱門')
    dom = requests.get("https://www.appledaily.com.tw/realtime/hot/").text
    soup = BeautifulSoup(dom, 'html5lib')
    for ele in soup.find_all("div", "flex-feature"):
        print("Link: ", ele.a.attrs["href"])
        print("Time: ", ele.a.find("div", "timestamp").text)
        print("Title: ", ele.a.find("span", "headline").text)
        print("---")

    print('**********')
    
    print('自由今日熱門')
    dom = requests.get('https://news.ltn.com.tw/list/breakingnews/popular').text
    soup = BeautifulSoup(dom, 'html5lib')
    for ele in soup.find('ul', 'list').find_all('li'):
        if ele.find('a', 'tit'):
            print("Link: ", ele.find('a', 'tit').attrs["href"])        
            print("Time: ", ele.find('a', 'tit').span.text)
            print("Title: ", ele.find('a', 'tit').div.h3.text)
            print("---")

if __name__ == '__main__':
    main()
