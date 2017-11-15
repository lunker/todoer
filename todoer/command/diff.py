from command.interface import AbstractHandler
from git.helper import GitHelper
from comment.parser import Parser
from console import Console


class Diff(AbstractHandler):
    def handle(self, *args, **kwargs):
        diff_content = GitHelper.diff_current_dir()
        comment_list = Parser.parse_comment_from_git(diff_content)

        Console.get_instance().print(comment_list)

        pass
