import unittest
import reader


class TestReader(unittest.TestCase):

    def setUp(self):
        self.reader = reader.Reader()
        pass

    def tearDown(self):
        pass

    def test_get_project_root(self):
        root_path = self.reader.get_project_root()
        # print(root_path)
        self.assertEqual(root_path, '/Users/voiceloco/work/pythonspace/todoer', 'return right project path')
        pass

    def test_read_source(self):
        # root_path = self.reader.get_project_root()

        src_path = '/Users/voiceloco/work/pythonspace/todoer/todoer'
        self.reader.search_git_project(src_path)

        pass

    def test_find_comment(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReader)
    unittest.TextTestRunner(verbosity=2).run(suite)
