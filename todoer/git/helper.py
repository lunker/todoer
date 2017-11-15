from subprocess import Popen, PIPE
from util.file import FileUtil
import os


class GitHelper:

    @staticmethod
    def diff_current_dir():
        git_command = ['/usr/local/bin/git', 'diff', '.']
        result = GitHelper.__run_command(git_command)

        return result

    @staticmethod
    def diff_file(fd):
        git_command = ['/usr/local/bin/git', 'diff', fd]
        result = GitHelper.__run_command(git_command)

        return result

    @staticmethod
    def status():
        git_command = ['/usr/local/bin/git', 'status', '.']

        result = GitHelper.__run_command(git_command)

        return result

    @staticmethod
    def search():
        commits = GitHelper.__get_commit_id()
        commit_list = commits.split('\n')

        git_command = ['/usr/local/bin/git', 'grep', '-n',  r"# todo.*"]

        commit_list = commit_list[:len(commit_list)-1]
        git_command.extend(commit_list)

        result = GitHelper.__run_command(git_command)

        return result

    @staticmethod
    def __get_commit_id():
        git_command = ['/usr/local/bin/git', 'rev-list', '--all']
        result = GitHelper.__run_command(git_command)

        return result

    @staticmethod
    def __run_command(git_command):
        current_dir = os.getcwd()

        git_query = Popen(git_command, cwd=current_dir, stdout=PIPE, stderr=PIPE)
        (git_status, error) = git_query.communicate()
        if git_query.poll() == 0:
            # None
            # print(git_status.decode("unicode_escape"))
            return git_status.decode("unicode_escape")


if __name__ == '__main__':
    # Console.get_instance().print(GitHelper.search())
    pass