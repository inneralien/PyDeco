from NullHandler import NullHandler
from Exceptions import *
import logging

class TestClass():
    def __init__(self):
        self.logger = logging.getLogger("TestClass")
        h = NullHandler()
        logging.getLogger("TestClass").addHandler(h)
