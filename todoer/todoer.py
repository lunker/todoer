#!/usr/bin/python
from reader import Reader
import pickle
import os
import sys, getopt
from console import Console


class Application:

    def __init__(self):
        self.reader = Reader()

    def install(self):
        install_path = '/Users/voiceloco/work/pythonspace/todoer/.todoer'
        if not os.path.exists(install_path):
            os.mkdir('/Users/voiceloco/work/pythonspace/todoer/.todoer')

    def generate_todo_list(self):
        src_path = '/Users/voiceloco/work/pythonspace/todoer/todoer'
        comment_list = self.reader.search_git_project(src_path)

        for comment in comment_list:
            # save comment
            print(comment)

        with open('/Users/voiceloco/work/pythonspace/todoer/.todoer/comments', 'wb') as f:
            pickle.dump(comment_list, f)


    def load(self):
        # todo

        with open('/Users/voiceloco/work/pythonspace/todoer/.todoer/comments', 'rb') as f:
            r = pickle.load(f)

        return r

    @staticmethod
    def run():
        try:
            print("ruy1")
            # 여기서 입력을 인자를 받는 파라미터는 단일문자일 경우 ':' 긴문자일경우 '='을끝에 붙여주면됨
            opts, args = getopt.getopt(sys.argv[1:], "abchi:o:", ["input=", "output=", "help"])

        except getopt.GetoptError as err:
            print
            str(err)
            help()
            sys.exit(1)

        for opt, arg in opts:

            if (opt == "-a"):
                print("a option enabled")
            elif (opt == "-b"):
                print("b option enabled")


if __name__ == '__main__':
    Application.run()



