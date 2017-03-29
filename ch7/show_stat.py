import json
import os
from matplotlib import pyplot as plt


def get_avg_price(json_data):
    sum = 0
    for item in json_data:
        sum += int(item['price'])
    return sum/len(json_data)


if __name__ == '__main__':
    json_files = [f for f in os.listdir('json')
                  if os.path.isfile(os.path.join('json', f)) and f.endswith('.json')]

    avg_prices_momo = dict()
    avg_prices_pchome = dict()
    for json_file in json_files:
        with open(os.path.join('json', json_file), 'r', encoding='utf-8') as f:
            data = json.load(f)
            date = data['date']
            if data['store'] == 'momo':
                avg_prices_momo[date] = get_avg_price(data['items'])
            elif data['store'] == 'pchome':
                avg_prices_pchome[date] = get_avg_price(data['items'])

    # 排序日期
    keys = avg_prices_momo.keys()
    date = sorted(keys)
    print('momo')
    for d in date:
        print(d, int(avg_prices_momo[d]))
    print('pchome')
    for d in date:
        print(d, int(avg_prices_momo[d]))

    # x-axis
    x = [int(i) for i in range(len(date))]
    plt.xticks(x, date)  # 將 x-axis 用字串標註
    price_momo = [avg_prices_momo[d] for d in date]  # y1-axis
    price_pchome = [avg_prices_pchome[d] for d in date]  # y2-axis
    plt.plot(x, price_momo, marker='o', linestyle='solid')
    plt.plot(x, price_pchome, marker='o', linestyle='solid')
    plt.legend(['momo', 'pchome'], loc='upper left')
    # specify values on ys
    for a, b in zip(x, price_momo):
        plt.text(a, b, str(int(b)))
    for a, b in zip(x, price_pchome):
        plt.text(a, b, str(int(b)))
    plt.show()
