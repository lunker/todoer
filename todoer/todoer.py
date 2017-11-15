#!/usr/bin/python
from command.command import PreProcessor, Dispatcher, PostProcessor
from reader import Reader
import pickle
import os
import sys, getopt, subprocess, errno
from console import Console
from util.file import FileUtil
from util.singleton import Singleton
from git.helper import GitHelper
import command.command
import util.file


class Application(metaclass=Singleton):

    def run(self):

        # print("""#######
   #     ####  #####   ####  ###### #####  
   #    #    # #    # #    # #      #    # 
   #    #    # #    # #    # #####  #    # 
   #    #    # #    # #    # #      #####  
   #    #    # #    # #    # #      #   #  
   #     ####  #####   ####  ###### #    # """)

        args = sys.argv

        command = PreProcessor.handle(args)
        Dispatcher.handle(command)
        # PostProcessor.handle()

if __name__ == '__main__':
    Application().run()



