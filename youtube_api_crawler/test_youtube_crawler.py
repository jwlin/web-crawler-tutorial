# python standard module
import unittest

# youtube_crawler module
from youtube_crawler import YoutubeCrawler

# ddt module
from ddt import ddt, data, unpack, file_data


@ddt
class YoutubeCrawlerTest(unittest.TestCase):
    def setUp(self):
        self.yc = YoutubeCrawler()

    def tearDown(self):
        pass

    def test_crawl_search_result(self):
        mvs = self.yc.crawl_search_result('gun n roses')
        self.assertEqual(len(mvs) > 0, True)

if __name__ == '__main__':
    unittest.main()
