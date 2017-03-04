# requests module
import requests

# beautifulsoup module
from bs4 import BeautifulSoup

# python standard libs
import re


class YahooMovieCrawler(object):
    def __init__(self):
        self.movies = []

    def crawl_search_result(self, query):
        url = 'https://tw.movies.yahoo.com/moviesearch_result.html?k={0}'.format(query)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        movies = []
        elems = []
        elems_row = soup.find_all('div', class_='clearfix row')
        elems_row_last = soup.find_all('div', class_='clearfix row_last')
        elems.extend(elems_row)
        elems.extend(elems_row_last)
        for elem in elems:
            movie = {}
            movie['chinese_name'] = elem.find('div', class_='text').find('h4').text
            movie['english_name'] = elem.find('div', class_='text').find('h5').text
            movie['yahoo_movie_link'] = elem.find('div', class_='img').find('a')['href']
            movie['yahoo_id'] = self.find_movie_id(movie['yahoo_movie_link'])
            movie['yahoo_poster'] = elem.find('div', class_='img').find('img')['src'].replace('mpost4', 'mpost')
            release_data = elem.find('div', class_='text').find('span').text
            movie['yahoo_release_data'] = self.change_time_format(release_data)
            movie['yahoo_favorite'] = elem.find('div', class_='bd').find('em').text
            movie['yahoo_description'] = elem.find('p').text.replace(u'...詳全文', '')
            movie['yahoo_trailer'] = elem.find('li', class_='trailer').find('a')['href']
            movies.append(movie)
        # for m in movies:
        #     print (m['yahoo_id'], m['chinese_name'], m['yahoo_description'])
        return movies

    def crawl_movie_thisweek_comingsoon(self, mode):
        if mode == 'movie_thisweek':
            url = 'https://tw.movies.yahoo.com/movie_thisweek.html'
        elif mode == 'movie_comingsoon':
            url = 'https://tw.movies.yahoo.com/movie_comingsoon.html'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        movies = []
        elems = []
        elems_group_date = soup.find('div', class_='group-date')
        elems_row = soup.find_all('div', class_='clearfix row')
        elems_row_last = soup.find_all('div', class_='clearfix row_last')
        elems.extend(elems_row)
        elems.extend(elems_row_last)
        for elem in elems:
            movie = {}
            movie['chinese_name'] = elem.find('div', class_='text').find('h4').text
            movie['english_name'] = elem.find('div', class_='text').find('h5').text
            movie['yahoo_movie_link'] = elem.find('div', class_='img').find('a')['href']
            movie['yahoo_id'] = self.find_movie_id(movie['yahoo_movie_link'])
            movie['yahoo_poster'] = elem.find('div', class_='img').find('img')['src'].replace('mpost4', 'mpost')
            release_data = elem.find('div', class_='text').find('span').text
            movie['yahoo_release_data'] = self.change_time_format(release_data)
            try:
                movie['yahoo_favorite'] = elem.find('div', class_='bd').find('em').text
            except AttributeError:
                movie['yahoo_favorite'] = ''
            movie['yahoo_description'] = elem.find('p').text.replace(u'...詳全文', '').replace('\n', '')
            if mode == 'movie_thisweek':
                movie['date_new_film'] = elems_group_date.text
            elif mode == 'movie_comingsoon':
                movie['date_comingsoon'] = elems_group_date.text
            movies.append(movie)

        # for m in movies:
        #     print (m['yahoo_id'], m['chinese_name'], m['yahoo_description'])
        return movies

    def store_movies(self, movie):
        if movie is not None:
            self.movies.append(movie)

    def change_time_format(self, release_data):
        pat_time = '\d+-\d+-\d+'
        match = re.search(pat_time, release_data)
        if match is None:
            return release_data
        else:
            return match.group(0)

    def change_rank_time_format(self, rank_time):
        # 2016-12-31 ~ 2017-01-01
        # 2017-01-07 ~ 01-08
        pat_time = '\d+-\d+-\d+ ~ \d+-\d+-\d+'
        match = re.search(pat_time, rank_time)
        if match is None:
            return rank_time
        else:
            rank_time = match.group(0).split()
            return rank_time[0] + ' ' + rank_time[2]

    def find_movie_id(self, url):
        pat_id = '/id=\d+'
        match = re.search(pat_id, url)
        if match is None:
            return url
        else:
            return match.group(0).replace('/id=', '')


def main():
    ymc = YahooMovieCrawler()
    ymc.crawl_search_result('刺客')
    ymc.crawl_movie_thisweek_comingsoon('movie_thisweek')
    ymc.crawl_movie_thisweek_comingsoon('movie_comingsoon')


if __name__ == '__main__':
    main()
