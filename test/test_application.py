import unittest
from app import Application

class TestApplication(unittest.TestCase):

    def setUp(self):
        self.app = Application()
        pass

    def tearDown(self):
        pass

    def test_install(self):
        self.app.install()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApplication)
    unittest.TextTestRunner(verbosity=2).run(suite)
