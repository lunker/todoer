import unittest
import reader
from util.file import FileUtil


class TestUtil(unittest.TestCase):

    def setUp(self):
        self.reader = reader.Reader()
        pass

    def tearDown(self):
        pass

    def test_util(self):
        root_path = FileUtil.find_project_root()
        print(root_path)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtil)
    unittest.TextTestRunner(verbosity=2).run(suite)
