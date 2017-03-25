import requests
import json
import math
from collections import Counter


OMDB_URL = 'http://www.omdbapi.com'


def get_data(url):
    data = json.loads(requests.get(url).text)
    if data['Response'] == 'True':
        return data
    else:
        return None


def search_ids_by_keyword(keywords):
    movie_ids = list()
    query = '+'.join(keywords.split())  # e.g., "Iron Man" -> Iron+Man
    url = OMDB_URL + '/?s=' + query
    data = get_data(url)
    ''' e.g.,
    {
      "Search": [
        {
          "Title": "Iron Man",
          "Year": "2008",
          "imdbID": "tt0371746",
          "Type": "movie",
          "Poster": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SX300.jpg"
        },
        ...
      ],
      "totalResults": "81",
      "Response": "True"
    }
    '''
    if data:
        # 取得第一頁電影 id
        for item in data['Search']:
            movie_ids.append(item['imdbID'])
        # 取得搜尋結果總數
        total = int(data['totalResults'])
        num_pages = math.floor(total/10) + 1

        # 取得第二頁以後的資料
        for i in range(2, num_pages+1):
            url = OMDB_URL + '/?s=' + query + '&page=' + str(i)
            data = get_data(url)
            if data:
                for item in data['Search']:
                    movie_ids.append(item['imdbID'])
    return movie_ids


def search_by_id(movie_id):
    url = OMDB_URL + '/?i=' + movie_id
    data = get_data(url)
    return data if data else None


if __name__ == '__main__':
    keyword = 'iron man'
    m_ids = search_ids_by_keyword(keyword)
    print('關鍵字 %s 共有 %d 部影片' % (keyword, len(m_ids)))
    print('取得影片資料中...')
    movies = list()
    for m_id in m_ids:
        movies.append(search_by_id(m_id))
    print('影片資料範例')
    for m in movies[:3]:
        print(m)
    years = [m['Year'] for m in movies]
    # collections.Counter() 會統計一個 list 中各項目出現的次數, 並回傳一個 dict
    year_dist = Counter(years)
    print('發行年份分布:', year_dist)
    # 如果該電影的 'imdbRating' 欄位不是 'N/A' 則轉換其值為 float 並放入 ratings 內
    ratings = [float(m['imdbRating']) for m in movies if m['imdbRating'] != 'N/A']
    print('平均評分:', sum(ratings)/len(ratings))
