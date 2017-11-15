import os
import re
from comment.comment import Comment


class Reader:

    def __init__(self):
        self.except_dir_list = [
            'bin',
            'include',
            'lib'
        ]



    def search_git_project(self, root_path):
        """
        
        :param root_path: 
        :return: comment_list
        :rtype: list of Comment
        """
        comment_list = list()

        for python_src in self.__file_system_search(root_path):
            comment_list.extend(self.find_comment(python_src, 'todo'))

        return comment_list

    def __file_system_search(self, root_path):
        """
            Generate python source path 
         
        :param root_path: 
        :return: source_file
        :rtype str
        """

        current_dirs = os.listdir(root_path)

        for fd in current_dirs:
            full_path = root_path + "/" + fd

            if os.path.isfile(full_path):
                # File
                if '.py' in full_path:
                    yield full_path
            else:
                # Directory
                if fd in self.except_dir_list:
                    yield from self.__file_system_search(full_path)