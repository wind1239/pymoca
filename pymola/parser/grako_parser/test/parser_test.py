import unittest
import pprint

from ..parser import ModelicaParser


class Test(unittest.TestCase):

    def setUp(self):
        self.parser = ModelicaParser()
        pass

    def basic_test(self):
        ast = self.parser.parse('''
            class test "hello world \a \b \f \r"
                flow a;
            end test;

            class test2
            end test2;
        ''', rule_name='stored_definition', trace=False)
        pprint.pprint(ast)

