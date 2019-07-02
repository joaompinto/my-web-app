from quickweb import controller
from random import randint

class Controller(object):

    @controller.publish
    def default(self, *args, **kwargs):
        return "Python is cool "+str(randint(0, 100))
