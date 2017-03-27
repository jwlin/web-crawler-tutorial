# coding=utf-8

import html
import json
import time
import math
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

from web_util import request_url


def st_ruten(query, first_page=1, last_page=1, low_price=-1, high_price=-1):
    # return item list. note that item list is NOT the same order as pages
    item_list = []
    try:
        query_enc = urllib.parse.quote(query)
    except TypeError:
        return []

    base_url = "http://m.ruten.com.tw/ajax/get_search_list.php?k=" + query_enc
    print(base_url)

    query_url = base_url
    if low_price != -1 or high_price != -1:
        if low_price == -1:
            low_price = 1
        if high_price == -1:
            high_price = 1000000
        query_url = base_url + "&p1=" + str(low_price) + "&p2=" + str(high_price)

    req = request_url(query_url)
    if req is None:
        return []

    try:
        json_dict = json.loads(req.text)
        if json_dict.get('goods') is None \
                or json_dict.get('goods').get('total') is None:
            return []
    except Exception as e:
        print(e)
        return []

    total_item_count = int(json_dict['goods']['total'])
    total_page_count = int(math.ceil(total_item_count / 10.0))

    # if only request page 1, use downloaded data is enough
    if first_page == 1:
        return parse_items_from_json(json_dict)

    page_url_list = []

    cur_page = first_page
    while cur_page <= min(last_page, total_page_count):
        cur_page_url = base_url
        if low_price > 0 and high_price > 0:
            cur_page_url += "&p1=" + str(low_price) + "&p2=" + str(high_price)

        cur_page_url += '&p=' + str(cur_page)
        # print(cur_page_url)
        page_url_list.append(cur_page_url)
        cur_page += 1

    # fetch pages in parallel
    thread_limit = 16
    num_of_task = len(page_url_list)
    num_of_thread = min(num_of_task, thread_limit)
    executor = ThreadPoolExecutor(max_workers=num_of_thread)
    async_task = [None] * num_of_thread

    task_index = 0
    num_of_running_thread = 0
    all_thread_done = False
    task_id = [None] * num_of_thread
    task_finished = [False] * num_of_thread

    while not all_thread_done:
        for i in range(0, num_of_thread):
            # print('i = ', i, ' num_of_running_thread = ', num_of_running_thread)
            if async_task[i] is None or async_task[i].done():
                if async_task[i] is not None:
                    # task done, get return value
                    if not task_finished[task_id[i]]:
                        # print('get async_task[', i, ']')
                        # print(async_task[i].result())
                        item_list.extend(async_task[i].result())
                        task_finished[task_id[i]] = True
                        num_of_running_thread -= 1

                if task_index < num_of_task:
                    # assign new task
                    task_id[i] = task_index
                    async_task[i] = executor.submit(st_rutun_page, page_url_list[task_index])
                    task_index += 1
                    num_of_running_thread += 1

            if num_of_running_thread == 0:
                # exit when all threads are done
                all_thread_done = True
                break

    return item_list


def st_rutun_page(page_url):
    response = request_url(page_url)
    if response is None:
        print('Error: response is None. url=', page_url)
        return []

    response.encoding = 'utf-8'
    item_list = parse_items_from_json(response.json())
    return item_list


def parse_items_from_json(json_dict):
    item_list = list()
    item_objects = json_dict['goods']['item']
    for item_obj in item_objects:
        item = dict()
        item['name'] = html.unescape(item_obj['name'])
        item['price'] = int(item_obj['direct_price'])
        item['img_url'] = item_obj['img_path']
        item['url'] = 'http://goods.ruten.com.tw/item/show?' + item_obj['no']
        item['store'] = 'ruten'
        item_list.append(item)
    return item_list


def main():
    out_file = open('search_result_ruten.txt', mode='w', encoding='utf-8')
    search_query = 'iphone 7'
    item_list = st_ruten(search_query, low_price=100)
    print(search_query)
    print('len(item_list) = ', len(item_list))
    out_file.write('q = ' + search_query + '\n')
    out_file.write('len(item_list) = ' + str(len(item_list)) + '\n')
    for item in item_list:
        data_string = (str(item['price']) + ', ' + item['name'] + ' ' + item['url'])
        print(data_string)
        out_file.write(data_string + '\n')
    out_file.close()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print('execution time = ' + "{:10.4f}".format(end - start) + ' sec')
