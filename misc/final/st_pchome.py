# coding=utf-8

import html
import json
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

from web_util import request_url


def st_pchome(query, first_page=1, last_page=1, low_price=-1, high_price=-1):
    # return item list. note that item list is NOT the same order as pages
    item_list = []
    query_enc = urllib.parse.quote(query)
    base_url = "http://ecshweb.pchome.com.tw/search/v3.3/all/results?q=" + query_enc + "&sort=rnk"

    if low_price != -1 or high_price != -1:
        if low_price == -1:
            low_price = 1
        if high_price == -1:
            high_price = 1000000
        query_url = base_url + "&price=" + str(low_price) + "-" + str(high_price)
    else:
        query_url = base_url

    req = request_url(query_url)
    if req is None:
        return []
    req.encoding = 'utf-8'
    json_dict = json.loads(req.text)

    if json_dict.get('prods') is None:
        return []
        
    total_item_count = int(json_dict['totalRows'])
    total_page_count = int(json_dict['totalPage'])

    # if only request page 1, use downloaded data is enough
    if first_page == 1:
        return parse_items_from_json(json_dict)

    page_url_list = []

    cur_page = first_page
    while cur_page <= min(last_page, total_page_count):
        cur_page_url = base_url
        if low_price > 0 and high_price > 0:
            cur_page_url += "&price=" + str(low_price) + "-" + str(high_price)

        cur_page_url += '&page=' + str(cur_page)
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
            # print 'i = ', i, ' num_of_running_thread = ', num_of_running_thread
            if async_task[i] is None or async_task[i].done():
                if async_task[i] is not None:
                    # task done, get return value
                    if not task_finished[task_id[i]]:
                        # print 'get async_task[', i, ']'
                        item_list.extend(async_task[i].result())
                        task_finished[task_id[i]] = True
                        num_of_running_thread -= 1

                if task_index < num_of_task:
                    # assign new task
                    task_id[i] = task_index
                    async_task[i] = executor.submit(st_pchome_page, page_url_list[task_index])
                    task_index += 1
                    num_of_running_thread += 1

            if num_of_running_thread == 0:
                # exit when all threads are done
                all_thread_done = True
                break

    return item_list


def st_pchome_page(page_url):
    response = request_url(page_url)
    if response is None:
        print('Error: response is None. url=', page_url)
        return []

    response.encoding = 'utf-8'
    item_list = parse_items_from_json(response.json())
    return item_list


def parse_items_from_json(json_dict):
    item_list = list()
    item_objects = json_dict['prods']
    for item_obj in item_objects:
        try:
            item = dict()
            item['name'] = html.unescape(item_obj['name'])
            item['price'] = int(item_obj['price'])
            item['img_url'] = 'http://ec1img.pchome.com.tw/' + item_obj['picS']
            item['url'] = 'http://24h.pchome.com.tw/prod/' + item_obj['Id']
            item['store'] = 'pchome'
            item_list.append(item)
        except Exception:
            pass
    return item_list


def main():
    out_file = open('search_result_pchome.txt', mode='w', encoding='utf-8')

    search_query = "iphone 7"
    item_list = st_pchome(search_query)
    print(search_query)
    print('len(item_list) = ', len(item_list))
    out_file.write('q = ' + search_query + '\n')
    out_file.write('len(item_list) = ' + str(len(item_list)) + '\n')
    for item in item_list:
        item_string = str(item['price']) + ', ' + item['name'] + ' ' + item['url']
        out_file.write(item_string + '\n')
        print(item_string)
    out_file.close()

    item_list_sorted = sorted(item_list, key=lambda i: i['price'])
    print(item_list_sorted[0:5])


if __name__ == "__main__":
    main()
