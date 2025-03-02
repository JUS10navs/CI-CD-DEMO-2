import unittest
from app import app 

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode(), "Hello World!")

    def test_hi(self):
        response = self.app.get('/hi')
        self.assertEqual(response.data.decode(), "Hi World!")

if __name__ == '__main__':
    unittest.main()