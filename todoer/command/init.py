from command.interface import AbstractHandler
from util.singleton import Singleton
from util.file import FileUtil
import pickle, os
from reader import Reader


class Init(AbstractHandler, metaclass=Singleton):

    def __init__(self):
        self.reader = Reader()
        self.install_dir = '.todoer'
        self.comments = 'comments'
        self.comment_path = "/".join([FileUtil.find_project_root(), self.install_dir, self.comments])
        pass

    def install(self):
        install_path = "/".join([FileUtil.find_project_root(), self.install_dir])

        if not os.path.exists(install_path):
            os.mkdir(install_path)

    def handle(self, *args, **kwargs):
        src_path = '/Users/voiceloco/work/pythonspace/todoer/todoer'
        comment_list = self.reader.search_git_project(src_path)

        self.install()

        with open(self.comment_path, 'wb+') as f:
            pickle.dump(comment_list, f)
        f.close()