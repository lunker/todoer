import unittest
from todoer import Application
from console import Console

class TestApplication(unittest.TestCase):

    def setUp(self):
        self.app = Application()
        pass

    def tearDown(self):
        pass

    def test_install(self):
        self.app.install()

    # def test_generate_todo_list(self):
    #     self.app.generate_todo_list()
    #
    # def test_load(self):
    #     comment_list = self.app.load()
    #     print("test load!")
    #     for comment in comment_list:
    #         Console.get_instance().print(comment)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApplication)
    unittest.TextTestRunner(verbosity=2).run(suite)
