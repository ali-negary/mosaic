import unittest
import utils
import pandas


class TestUtil(unittest.TestCase):

    def test_read_file(self):
        # normal situation
        correct_result0 = utils.read_file('test_cases/correct_test_read_file0.csv', ['student_id', 'student_name'])
        self.assertTrue(type(correct_result0), "<class 'pandas.core.frame.DataFrame'>")
        self.assertTrue(list(correct_result0.columns), ['student_id', 'student_name'])
        # file name is .txt instead of .csv
        correct_result1 = utils.read_file('test_cases/correct_test_read_file1.txt', ['student_id', 'student_name'])
        self.assertTrue(type(correct_result1), "<class 'pandas.core.frame.DataFrame'>")
        self.assertTrue(list(correct_result1.columns), ['student_id', 'student_name'])
        # the columns are not enough
        with self.assertRaises(Exception):
            utils.read_file('test_cases/incorrect_test_read_file0.txt', ['student_id', 'student_name'])




