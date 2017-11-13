from reader import Reader
import os

class Application:

    def __init__(self):
        self.reader = Reader()

    def install(self):
        os.mkdir('/Users/voiceloco/work/pythonspace/todoer/.todoer')

    def inspect(self):
        src_path = '/Users/voiceloco/work/pythonspace/todoer/todoer'
        comment_list = self.reader.search_git_project(self, src_path)



