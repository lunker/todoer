from command.interface import AbstractHandler
from comment.comment import Comment, CommentStatus
from console import Console
from util.file import FileUtil
from git.helper import GitHelper
import pickle
import re
from comment.parser import Parser
from enum import Enum


class Status(AbstractHandler):

    def __init__(self):
        self.install_dir = '.todoer'
        self.comments = 'comments'
        self.comment_path = "/".join([FileUtil.find_project_root(), self.install_dir, self.comments])

    def handle(self, *args, **kwargs):

        status_result = dict()

        result = GitHelper.status()

        modified_regex = re.compile('modified: .*')

        modified_file_list = modified_regex.findall(result)

        for file in modified_file_list:
            file_comment_list = list()

            file_name = self.__parse_file_name(file)

            raw_file_diff_data = GitHelper.diff_file(file_name)

            comment_message_list = Parser.parse_file_diff(raw_file_diff_data)

            if not comment_message_list:
                continue

            for comment_message in comment_message_list:
                comment_status = None

                if comment_message[0] == '+':
                    comment_status = CommentStatus.ADDED
                else:
                    comment_status = CommentStatus.DELETED

                file_comment_list.append(Comment(content=comment_message, status=comment_status, file_name=file_name))
            status_result[file_name] = file_comment_list

        Console.get_instance().print_status(status_result)

    def __parse_file_name(self, path):
        file_name = None

        file_name = path.split(':')[1]
        file_name = file_name.replace(' ', '')

        return file_name

