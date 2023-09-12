from unittest import TestCase
from function import app

class Test(TestCase):
    def test_handler(self):

        app.handler({'url1': 'https://finance.yahoo.com/quote/AAPL?p=AAPL'}, None)

