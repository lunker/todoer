from git import Repo
import unittest

class TestGit(unittest.TestCase):

    def setUp(self):

        pass

    def tearDown(self):
        pass

    def test_git(self):
        repo = Repo('/Users/voiceloco/work/pythonspace/todoer')
        hcommit = repo.head.commit
        # hcommit.diff()

        # Traverse added Diff objects only
        for diff_added in hcommit.diff('HEAD~1').iter_change_type('A'):
            print(diff_added)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGit)
    unittest.TextTestRunner(verbosity=2).run(suite)
