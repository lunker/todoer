#!/usr/bin/python
from reader import Reader
import pickle
import os
import sys, getopt, subprocess, errno
from console import Console
from util.file import FileUtil
from util.singleton import Singleton
import util.file



class Application(metaclass=Singleton):

    def __init__(self):
        self.reader = Reader()
        self.install_dir = '.todoer'
        self.comments = 'comments'
        self.comment_path = "/".join([FileUtil.find_project_root(), self.install_dir, self.comments])

    def install(self):
        install_path = "/".join([FileUtil.find_project_root(), self.install_dir])

        if not os.path.exists(install_path):
            os.mkdir(install_path)

    def init(self):
        src_path = '/Users/voiceloco/work/pythonspace/todoer/todoer'
        comment_list = self.reader.search_git_project(src_path)

        with open(self.comment_path, 'wb') as f:
            pickle.dump(comment_list, f)

    def generate_todo_list(self):
        src_path = '/Users/voiceloco/work/pythonspace/todoer/todoer'
        comment_list = self.reader.search_git_project(src_path)

        with open(self.comment_path, 'wb') as f:
            pickle.dump(comment_list, f)

    def load(self):
        # todo
        with open(self.comment_path, 'rb') as f:
            r = pickle.load(f)

        return r

    def print_todo_list(self):
        print("print todo list")

        comment_list = self.load()
        Console.get_instance().print(comment_list)

    def run(self):

        # print("""#######
   #     ####  #####   ####  ###### #####  
   #    #    # #    # #    # #      #    # 
   #    #    # #    # #    # #####  #    # 
   #    #    # #    # #    # #      #####  
   #    #    # #    # #    # #      #   #  
   #     ####  #####   ####  ###### #    # """)


        args = sys.argv

        for arg in args:
            if arg == 'list':
                print("Command: " + arg)
                self.print_todo_list()
            elif arg == 'init':
                self.init()


if __name__ == '__main__':
    Application().run()
    # Application().print_todo_list()

    '''
    try:
        pager = subprocess.Popen(['less', '-F', '-X'],
                                      stdin=subprocess.PIPE,
                                      stdout=sys.stdout)
        tmp = "asdfasfadsasddassfdas\n\n"*100000
        pager.stdin.write(bytes(tmp.encode('utf-8')))
        pager.stdin.close()
        pager.wait()
    except IOError as e:
        if e.errno == errno.EPIPE:
        # EPIPE error
            print("epipe error")
        else:
            print("other io error")
    '''


