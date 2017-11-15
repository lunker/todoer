from command.interface import AbstractHandler
from console import Console
from util.file import FileUtil
import pickle


class List(AbstractHandler):

    def __init__(self):
        self.install_dir = '.todoer'
        self.comments = 'comments'
        self.comment_path = "/".join([FileUtil.find_project_root(), self.install_dir, self.comments])

    def __load(self):
        # todo
        with open(self.comment_path, 'rb') as f:
            r = pickle.load(f)

        return r

    def handle(self, *args, **kwargs):
        comment_list = self.__load()
        Console.get_instance().print(comment_list)