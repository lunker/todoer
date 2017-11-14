class CommentFactory:

    @staticmethod
    def create_comment(type):
        return Comment()


class Comment:
    def __init__(self, comment_type, file_name, content, status):
        self.id = None
        self.comment_type = comment_type
        self.status = status
        self.file_name = file_name
        self.git_index = None
        self.start_line = None
        self.end_line = None
        self.content = content

        pass

    def __set__(self, instance, value):
        # print('set')
        pass

    # def __setattr__(self, key, value):
    #     print('setattr')
    #     print('key: {key}, value:{value}'.format(key=key, value=value))
    #     self.
    #     return self

    def set(self, *args, **kwargs):
        # print(kwargs)
        # print(kwargs.keys())
        print("Set chain!")

        for key in kwargs.keys():
            self.__setattr__(key, kwargs.get(key))
        # self.__setattr__(kwargs.keys()[0], kwargs.values()[0])

        return self

    def __str__(self):
        comment = "type: {type}, file_name: {file_name}, content: {content}".format(type=self.type, file_name=self.file_name, content=self.content)
        return comment


class Todo(Comment):
    pass

class Fixme(Comment):
    pass

if __name__ == '__main__':

    comment = Comment()
    comment.end_line = "asdf"
    comment.set(end_line=234).set(asdf=123)