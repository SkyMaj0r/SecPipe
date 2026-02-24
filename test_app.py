import unittest
from app import login

class TestApp(unittest.TestCase):
    def test_login_success(self):
        self.assertTrue(login("admin", "1234"))

    def test_login_failure(self):
        self.assertFalse(login("user", "wrongpass"))

if __name__ == '__main__':
    unittest.main()