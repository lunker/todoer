import os
import re
from comment import Comment

class Reader:

    def __init__(self):
        self.except_dir_list = [
            'bin',
            'include',
            'lib'
        ]

    def get_project_root(self):
        """
            find current project's root path 

        :return: git_path
        :rtype: str
        """

        git_path = None
        current_path = os.getcwd()

        for project_root_path in self.__upward(current_path):
            if '.git' in os.listdir(project_root_path):
                git_path = project_root_path
                break

        return git_path

    @staticmethod
    def __upward(path):
        """
            Find path of upward
            
        :param path:
        :type path: str
        :return: upward_path
        :rtype: str
        """

        occurrence = path.count('/')
        last_idx = len(path)

        for idx in range(occurrence):
            if last_idx != -1:
                yield path[:last_idx]
                last_idx = path.rfind('/', 0, last_idx)

    def find_comment(self, python_src, type):
        """ 
            Read Source file & find given type comments 
             
        :param python_src: Python file full path
        :type python_src: str
        :param type: comment type
        :type type: str (todo, fixme, hack . . . )
        :return: 
        """
        comment_list = list()
        todo_regex = re.compile('# ?[Tt]odo.*')

        with open(python_src) as f:
            source = f.read()

            result_list = todo_regex.findall(source)

            for result in result_list:
                print("todo comment ::\n" + result)
                comment = Comment('todo', 'test_file_name', result)
                comment_list.append(comment)

        f.closed

        return comment_list

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