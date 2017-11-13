class Comment:
    def __init__(self):
        self.type = None
        self.file_name = None
        self.start_line = None
        self.end_line = None
        self.content = None
        pass


class Todo(Comment):
    pass

class Fixme(Comment):
    pass