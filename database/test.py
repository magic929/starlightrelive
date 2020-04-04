import input
import unittest

class input_test(unittest.TestCase):
    def setUp(self):
        self.path = "./file/dress.lua.json"
    
    def read_file_test(self):
        result = input.read_file(self.path)
        print(result[1])