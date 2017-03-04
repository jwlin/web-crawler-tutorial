# python standard module
import unittest

# jarvis module
from yahoo_movie_crawler import YahooMovieCrawler

# ddt module
from ddt import ddt, data, unpack, file_data


@ddt
class YahooMovieCrawlerTest(unittest.TestCase):
    def setUp(self):
        self.ymc = YahooMovieCrawler()

    def tearDown(self):
        pass

    def test_crawl_search_result(self):
        movies = self.ymc.crawl_search_result('刺客')
        self.assertEqual(len(movies) > 0, True)

    def test_crawl_movie_thisweek_comingsoon(self):
        movies = self.ymc.crawl_movie_thisweek_comingsoon('movie_thisweek')
        self.assertEqual(len(movies) > 0, True)
        movies = self.ymc.crawl_movie_thisweek_comingsoon('movie_comingsoon')
        self.assertEqual(len(movies) > 0, True)

    def test_change_time_format(self):
        release_data = self.ymc.change_time_format('上映日期：2017-01-06')
        self.assertEqual(release_data, '2017-01-06')
        release_data = self.ymc.change_time_format('上映日期：2017--01--06')
        self.assertEqual(release_data, '上映日期：2017--01--06')

    def test_change_rank_time_format(self):
        box_time = self.ymc.change_rank_time_format('統計時間：2016-12-31 ~ 2017-01-01')
        self.assertEqual(box_time, '2016-12-31 2017-01-01')
        error_time = self.ymc.change_rank_time_format('統計時間：2017-01-07 ~ 01-08')
        self.assertEqual(error_time, '統計時間：2017-01-07 ~ 01-08')

    def test_find_movie_id(self):
        id = self.ymc.find_movie_id('https://tw.movies.yahoo.com/movieinfo_main.html/id=6530')
        self.assertEqual(id, '6530')
        id = self.ymc.find_movie_id('https://tw.movies.yahoo.com/movieinfo_main.html/id/=6530')
        self.assertEqual(id, 'https://tw.movies.yahoo.com/movieinfo_main.html/id/=6530')


if __name__ == '__main__':
    unittest.main()
