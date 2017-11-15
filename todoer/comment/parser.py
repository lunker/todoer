import re
from comment.comment import Comment


class Parser:

    @staticmethod
    def parse(data):


        pass

    @staticmethod
    def find_comment(self, python_src):
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
                # print("todo comment ::\n" + result)
                comment = Comment('todo', 'test_file_name', result, 'None status')
                comment_list.append(comment)

        f.closed

        return comment_list

    @staticmethod
    def parse_comment_from_git(data):

        comment_list = list()
        todo_regex = re.compile('# ?[Tt]odo.*')

        result_list = todo_regex.findall(data)

        for result in result_list:
            # print("todo comment ::\n" + result)
            comment = Comment('todo', 'test_file_name', result, 'None status')
            comment_list.append(comment)

        return comment_list

    @staticmethod
    def parse_file_diff(raw_file_diff):
        todo_regex = re.compile('[+|-] ?# ?[Tt]odo.*')

        result_list = todo_regex.findall(raw_file_diff)

        return result_list


