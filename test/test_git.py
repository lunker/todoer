from git import Repo
import unittest

from subprocess import Popen, PIPE
from os import path
import re

class TestGit(unittest.TestCase):

    def setUp(self):

        pass

    def tearDown(self):
        pass

    def test_git(self):
        # repo = Repo('/Users/voiceloco/work/pythonspace/todoer')
        repo = Repo('/Users/voiceloco/work/pythonspace/lunker_cli')
        hcommit = repo.head.commit

        # Traverse added Diff objects only#
        for diff_added in hcommit.diff_current_dir(None, '/Users/voiceloco/work/pythonspace/lunker_cli/src/App.py').iter_change_type('M'):
            # print ()
            print(diff_added)
            pass

        git_command = ['/usr/local/bin/git', 'diff', '/Users/voiceloco/work/pythonspace/lunker_cli/src/App.py']
        # repository = path.dirname('/Users/voiceloco/work/pythonspace/lunker_cli')
        repository = '/Users/voiceloco/work/pythonspace/lunker_cli'

        git_query = Popen(git_command, cwd=repository, stdout=PIPE, stderr=PIPE)
        (git_status, error) = git_query.communicate()
        if git_query.poll() == 0:
            print(git_status.decode("unicode_escape"))

        test_diff = git_status.decode("unicode_escape")

        added_regex = re.compile("\+ ?.*")

        result_list = added_regex.findall(test_diff)
        if result_list is not None:
            for result in result_list:
                print(result)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGit)
    unittest.TextTestRunner(verbosity=2).run(suite)
