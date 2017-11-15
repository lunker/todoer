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
    @staticmethod
    def handle(command):
        """
        
        :param command: Todoer command
        :type command: Command
        :param data: 
        :return: 
        """
        if command.command == 'diff':
            Diff().handle(command=command)
            pass
        elif command.command == 'list':
            List().handle(command=command)
            pass
        elif command.command == 'init':
            Init().handle(command=command)
        elif command.command == 'status':
            # GitHelper.status()
            Status().handle()
        elif command.command == 'search':
            Search().handle()

