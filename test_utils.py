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
            utils.read_file('test_cases/incorrect_test_read_file1.csv')

    def test_csv2json(self):
        # normal situation
        correct_case = pandas.read_csv('test_cases/correct_test_csv2json0.csv', index_col=0)
        for student in utils.csv2json(correct_case)['students']:
            self.assertTrue(list(student.keys()), ['id', 'name', 'totalAverage', 'courses'])
            self.assertGreater(len(student['courses']), 0)
            self.assertTrue(student['totalAverage'], float)
            for course in student['courses']:
                self.assertTrue(course['courseAverage'], float)
        #  values are nan (empty indexed rows) - I wrote this really quick. so this might not be a good test.
        misshaped_case = pandas.read_csv('test_cases/misshaped_test_csv2json0.csv', index_col=0)
        for student in utils.csv2json(misshaped_case)['students']:
            self.assertTrue(list(student.keys()), ['id', 'name', 'totalAverage', 'courses'])
            self.assertGreater(len(student['courses']), 0)
            self.assertTrue(student['totalAverage'], float)
