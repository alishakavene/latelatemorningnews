import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.news_article = News('KCSE and KCPE post-poned to 2021','MInister of Educaation Addresses the Future Of Education During Covid','https://pbs.twimg.com/media/EcU9XvoXYAAPvXa?format=png&name=small')
        def test_instance(self):
            self.assertTrue(isinstance(self.news_article,News))

            
if __name__ == '__main__':
    unittest.main()