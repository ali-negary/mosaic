""" write sth in here
"""

import pandas as pd
import json


# This method gets the path to the csv file and the column used for indexing and returns a pandas' dataframe.
def read_file(path_to_csv, column_names, index=None):
    return pd.read_csv(path_to_csv, names=column_names, header=0)


# This method saves the JSON file in the desired path.
def save_results(result, path):
    output_file = open(path, 'w')
    output_file.write(json.dumps(result))
    return None


# This method checks if the weights
def check_weights(tests, marks):
    marks_tests = pd.merge(marks, tests, how='left', on="test_id").drop(labels=['test_id', 'test_mark'], axis=1)
    marks_tests = marks_tests.groupby(['course_id', 'student_id']).sum()
    return (marks_tests['test_weight'] == 100).all()


# This method calculates the average of students grades and maybe construct the json output.
def calculate_grades(courses, students, tests, marks):
    print("___________________marks_tests________________________")
    marks_tests = pd.merge(marks, tests, how='left', on="test_id")
    # This gives us the weighted marks for each student.
    marks_tests['weighted_marks'] = marks_tests['test_mark'] * marks_tests['test_weight'] / 100
    print(marks_tests)
    print("___________________sum_of_all________________________")
    # This gives us the sum of all courses for each student.
    sum_of_all = marks_tests.groupby(['student_id']).sum()
    print(sum_of_all)
    print("_____________________sum_per_course______________________")
    sum_per_course = marks_tests.groupby(['student_id', 'course_id']).sum()
    print(sum_per_course)
    print("____________________sum_per_course_______________________")
    sum_per_course = pd.merge(sum_per_course, courses, how='left', on="course_id")
    print(sum_per_course)
    print("_______________________________JSON XXX_______________________________")
    print(sum_per_course.to_json(orient='records'))
    results = {}
    return results
