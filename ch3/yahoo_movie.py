import requests
import re
import json
from bs4 import BeautifulSoup


Y_MOVIE_URL = 'https://tw.movies.yahoo.com/movie_thisweek.html'

# 以下網址後面加上 "/id=MOVIE_ID" 即為該影片各項資訊
Y_INTRO_URL = 'https://tw.movies.yahoo.com/movieinfo_main.html'  # 詳細資訊
Y_PHOTO_URL = 'https://tw.movies.yahoo.com/movieinfo_photos.html'  # 劇照
Y_TIME_URL = 'https://tw.movies.yahoo.com/movietime_result.html'  # 時刻表


def get_web_page(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_movies(dom):
    soup = BeautifulSoup(dom, 'html5lib')
    movies = []
    rows = soup.find_all('div', 'release_info_text')
    for row in rows:
        movie = dict()
        movie['expectation'] = row.find('div', 'leveltext').span.text.strip()
        movie['ch_name'] = row.find('div', 'release_movie_name').a.text.strip()
        movie['eng_name'] = row.find('div', 'release_movie_name').find('div', 'en').a.text.strip()
        movie['movie_id'] = get_movie_id(row.find('div', 'release_movie_name').a['href'])
        movie['poster_url'] = row.parent.find_previous_sibling('div', 'release_foto').a.img['src']
        movie['release_date'] = get_date(row.find('div', 'release_movie_time').text)
        movie['intro'] = row.find('div', 'release_text').text.replace(u'詳全文', '').strip()
        trailer_a = row.find_next_sibling('div', 'release_btn color_btnbox').find_all('a')[1]
        movie['trailer_url'] = trailer_a['href'] if 'href' in trailer_a.attrs.keys() else ''
        movies.append(movie)
    return movies


def get_date(date_str):
    # e.g. "上映日期：2017-03-23" -> match.group(0): "2017-03-23"
    pattern = '\d+-\d+-\d+'
    match = re.search(pattern, date_str)
    if match is None:
        return date_str
    else:
        return match.group(0)


def get_movie_id(url):
    # 20180515: URL 格式有變, e.g., 'https://movies.yahoo.com.tw/movieinfo_main/%E6%AD%BB%E4%BE%8D2-deadpool-2-7820.html
    # e.g., "https://tw.rd.yahoo.com/referurl/movie/thisweek/info/*https://tw.movies.yahoo.com/movieinfo_main.html/id=6707"
    #       -> match.group(0): "/id=6707"
    try:
        movie_id = url.split('.html')[0].split('-')[-1]
    except:
        movie_id = url
    return movie_id


def get_trailer_url(url):
    # e.g., 'https://tw.rd.yahoo.com/referurl/movie/thisweek/trailer/*https://tw.movies.yahoo.com/video/美女與野獸-最終版預告-024340912.html'
    return url.split('*')[1]


def get_complete_intro(movie_id):
    page = get_web_page(Y_INTRO_URL + '/id=' + movie_id)
    if page:
        soup = BeautifulSoup(page, 'html5lib')
        infobox = soup.find('div', 'gray_infobox_inner')
        print(infobox.text.strip())


def main():
    page = get_web_page(Y_MOVIE_URL)
    if page:
        movies = get_movies(page)
        for movie in movies:
            print(movie)
            # get_complete_intro(movie["movie_id"])
        with open('movie.json', 'w', encoding='utf-8') as f:
            json.dump(movies, f, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    main()