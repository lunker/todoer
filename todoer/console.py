from comment import Comment
import sys, subprocess, os
import logging
from termcolor import colored

POWERLINE_STYLE = True

class ColorLogFormatter(logging.Formatter):
    level_colors = {
        logging.DEBUG: 'cyan',
        logging.INFO: 'green',
        logging.WARNING: 'yellow',
        logging.ERROR: 'red',
        logging.CRITICAL: 'red',
    }


    def _get_exc_info(self, record):
        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            try:
                return str(record.exc_text)
            except UnicodeError:
                # Sometimes filenames have non-ASCII chars, which can lead
                # to errors when s is Unicode and record.exc_text is str
                # See issue 8924.
                # We also use replace for when there are multiple
                # encodings, e.g. UTF-8 for the filesystem and latin-1
                # for a script. See issue 13232.
                return record.exc_text.decode(sys.getfilesystemencoding(),
                                              'replace')
        return None

    def format(self, record):
        """Format logs nicely"""

        color = self.level_colors.get(record.levelno, 'white')

        levelname = colored(' {0:<6} '.format(record.levelname),
                            color, attrs=['reverse'])

        if POWERLINE_STYLE:
            levelname += colored(u'\ue0b0', color, 'on_white')

        loggername = colored(' {0} '.format(record.name), 'red', 'on_white')

        if POWERLINE_STYLE:
            loggername += colored(u'\ue0b0', 'white')

        message = colored(record.getMessage(), color)

        # parsing record as formatting

        s = ' '.join((''.join((levelname, loggername)), message))

        exc_info = self._get_exc_info(record)
        if exc_info is not None:
            if s[-1:] != "\n":
                s = s + "\n"
            s += colored(exc_info, 'grey', attrs=['bold'])

        return s


class Console:

    __instance = None

    def __init__(self):
        self.logger = logging.getLogger('console')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler(sys.stdout)
        self.handler.setFormatter(ColorLogFormatter())
        self.handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)
        self.pager = subprocess.Popen(['less', '-F', '-R', '-S', '-X', '-K'],
                                 stdin=subprocess.PIPE,
                                 stdout=sys.stdout)

    def pager(self, data):
        if type(data) is Comment:
            self.pager.stdin.write(data)
            self.pager.stdin.close()
            self.pager.wait()
        elif type(data) is list:
            for item in data:
                self.pager.stdin.write(item)
            self.pager.stdin.close()
            self.pager.wait()

        pass

    def print(self, data):

        if type(data) is Comment:
            self.logger.debug(data)
        elif type(data) is list:
            for item in data:
                self.logger.debug(item)

    def print_added(self):

        pass

    def print_deleted(self):
        pass

    def print_modified(self):
        pass


    @staticmethod
    def get_instance():
        """
        
        :return: instance
        :rtype: Console
        """
        if Console.__instance is None:
            Console.__instance = Console()

        return Console.__instance