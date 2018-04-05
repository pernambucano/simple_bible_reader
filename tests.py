import unittest
import flask

import main

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.app = main.mapp.test_client()

    def test_show_verse_for_today(self):
        page_result = self.app.get('/')
        self.assertIn(b'Salmos', page_result.data)

if __name__ ==  '__main__':
    unittest.main()
