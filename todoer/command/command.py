from command.init import Init
from command.list import List
from command.diff import Diff
from command.search import Search
from command.status import Status
from util.singleton import Singleton
from git.helper import GitHelper


class Command:
    def __init__(self, command=None, data=None):
        self.command = command
        self.data = data


class PreProcessor:
    @staticmethod
    def handle(args):
        """
            Valid Check & Create Command
        :param args: 
        :type args: list
        :return: 
        """

        command = Command()

        # command.command = args[0]
        command.command = args[1]
        return command


class PostProcessor:
    @staticmethod
    def handle(args):
        """
        
        :param args:
        :type args: list
        :return: command
        :rtype: Command
        """
        command = Command()

        for arg in args:
            if arg in ['list', 'diff']:
                command.command = arg

        return command


class Dispatcher:

    command_list = ['diff', 'list', 'init', 'status', 'search', 'help']

    @staticmethod
    def handle(command):
        """
        
        :param command: Todoer command
        :type command: Command
        :param data: 
        :return: 
        """

        if command.command in Dispatcher.command_list:
            class_name = list(command.command)
            class_name[0] = command.command[0].upper()
            class_name = ''.join(class_name)

            # handler = type(class_name, (), {})
            handler = globals()[class_name]
            handler().handle(command=command)
