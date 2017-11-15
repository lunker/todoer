from command.interface import AbstractHandler
from console import Console
from util.file import FileUtil
from git.helper import GitHelper
import pickle


class Search(AbstractHandler):

    def __init__(self):
        self.install_dir = '.todoer'
        self.comments = 'comments'
        self.comment_path = "/".join([FileUtil.find_project_root(), self.install_dir, self.comments])

    def handle(self, *args, **kwargs):
        result = GitHelper.search()
        Console.get_instance().print(result)
