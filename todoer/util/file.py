from util.singleton import Singleton
import os


class FileUtil:

    @staticmethod
    def find_project_root():
        """
                    find current project's root path 

                :return: git_path
                :rtype: str
                """

        git_path = None
        current_path = os.getcwd()

        for project_root_path in FileUtil.__upward(current_path):
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