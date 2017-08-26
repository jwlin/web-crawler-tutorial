import requests
import json
import time
import os
import numpy as np

category = {
    '55de818a9d1fa51000f94767': '生活',
    '55de818d9d1fa51000f94768': '藝術',
    '55de819a9d1fa51000f9476b': '運動',
    '55de81a49d1fa51000f9476e': '影音',
    '55de81a89d1fa51000f9476f': '手作',
    '55de81b79d1fa51000f94771': '其他',
    '55de81879d1fa51000f94766': '設計',
    '55de81929d1fa51000f94769': '科技',
    '55de81969d1fa51000f9476a': '商業',
    '55de819e9d1fa51000f9476c': '語言',
    '55de81a19d1fa51000f9476d': '烹飪',
    '55de81ac9d1fa51000f94770': '程式',
}


def crawl():
    # 初始 API: https://api.hahow.in/api/courses?limit=12&status=PUBLISHED
    # 接續 API: https://api.hahow.in/api/courses?latestId=54d5a117065a7e0e00725ac0&latestValue=2015-03-27T15:38:27.187Z&limit=30&status=PUBLISHED
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/59.0.3071.115 Safari/537.36'}
    url = 'https://api.hahow.in/api/courses'
    courses = list()
    resp_courses = requests.get(url + '?limit=30&status=PUBLISHED', headers=headers).json()
    while resp_courses:  # 有回傳資料則繼續下一輪擷取
        time.sleep(3)  # 放慢爬蟲速度
        courses += resp_courses
        param = '?latestId={0}&latestValue={1}&limit=30&status=PUBLISHED'.format(
            courses[-1]['_id'], courses[-1]['incubateTime'])
        resp_courses = requests.get(url + param, headers=headers).json()
    # 將課程資料存下來後續分析使用
    with open('hahow_courses.json', 'w', encoding='utf-8') as f:
        json.dump(courses, f, indent=2, sort_keys=True, ensure_ascii=False)
    return courses


if __name__ == '__main__':
    # 讀取資料檔 或 爬取並建立資料檔
    if os.path.exists('hahow_courses.json'):
        with open('hahow_courses.json', 'r', encoding='utf-8') as f:
            courses = json.load(f)
    else:
        courses = crawl()
    print('hahow 共有 %d 堂課程' % len(courses))

    # 取出程式類課程
    #programming_classes = [c for c in courses if '55de81ac9d1fa51000f94770' in c['categories']]

    # 取出程式類課程的募資價/上線價/學生數，並顯示統計資料
    pre_order_prices = list()
    prices = list()
    tickets = list()
    lengths = list()
    for c in courses:
        if '55de81ac9d1fa51000f94770' in c['categories']:
            pre_order_prices.append(c['preOrderedPrice'])
            prices.append(c['price'])
            tickets.append(c['numSoldTickets'])
            lengths.append(c['totalVideoLengthInSeconds'])
    print('平均募資價:', np.mean(pre_order_prices))
    print('平均上線價:', np.mean(prices))
    print('平均學生數:', np.mean(tickets))
    print('平均課程分鐘:', np.mean(lengths)/60)
    # print(np.corrcoef([tickets, pre_order_prices, prices, length]))
    corrcoef = np.corrcoef([tickets, pre_order_prices, prices, lengths])
    print('募資價與學生數之相關係數: ', corrcoef[0, 1])
    print('上線價與學生數之相關係數: ', corrcoef[0, 2])
    print('課程長度與學生數之相關係數: ', corrcoef[0, 3])