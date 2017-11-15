from util.singleton import Singleton


class AbstractHandler(metaclass=Singleton):
    def handle(self, *args, **kwargs):
        pass