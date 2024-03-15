import unittest
from app import app
from bs4 import BeautifulSoup

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Parse the HTML content
        soup = BeautifulSoup(response.data, 'html.parser')
        
        # Check for the presence of specific elements
        title_element = soup.find('title')
        self.assertIsNotNone(title_element)
        self.assertEqual(title_element.text, 'Big Star Collectibles')

if __name__ == '__main__':
    unittest.main()
