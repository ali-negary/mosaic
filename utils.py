""" This file provides the required tools for main.py to run.
        all methods expect reading from CLI is implemented here.
"""

import pandas as pd
import json


def read_file(path_to_csv, column_names):
    """
    "read_file" gets the path to the csv file and convert the csv into a pandas dataframe with the provided headers.
    :param path_to_csv: exact path to .csv file.
    :param column_names: a list of strings that will be the column headers of the output dataframe.
    :return: pandas dataframe
    """
    return pd.read_csv(path_to_csv, names=column_names, header=0)


def save_results(result_dict, path):
    """
    "save_results" gets a dictionary and saves it on the disk. The stored file will be in .json format.
    :param result_dict: the dictionary which should be saved in disk.
    :param path: the exact location on disk where the disk should be saved.
    :return: nothing.
    """
    output_file = open(path, 'w')
    output_file.write(json.dumps(result_dict))
    return None


def check_weights(tests, marks):
    """
    "check_weights" gets two dataframes of tests and marks. It will merge (join in SQL) them by test_id and removes the redundant columns.
    Next, the result will be grouped by course_id and then student_id and summation of test_wrights will be calculated.
    If all the records inside the test_weight column are equal to 100, it means the grades are valid.
    :param tests: records provided in tests.csv
    :param marks: records provided in marks.csv
    :return: True
    """
    marks_tests = pd.merge(marks, tests, how='left', on="test_id").drop(labels=['test_id', 'test_mark'], axis=1)
    marks_tests = marks_tests.groupby(['course_id', 'student_id']).sum()
    return (marks_tests['test_weight'] == 100).all()


def calculate_grades(courses, students, tests, marks):
    """
    "calculate_grades" gets 4 dataframes provided by the input .csv files and calculate the average of students' marks.
        - joins the marks and test on test_id.
        - calculates the weighted marks of the students based on test_marks and and their test_weights.
        - calculate the average of each student for all their courses (students_average).
        - calculate the marks of each student for each course (sum_per_course).
        - join student_average and sum_per_course to get a complete set of records.
    :return: a pandas dataframe with the following headers:
                student_id, course_id, weighted_marks, course_name, teacher_name, student_name, student_average
    """
    marks_tests = pd.merge(marks, tests, how='left', on="test_id")
    marks_tests['weighted_marks'] = marks_tests['test_mark'] * marks_tests['test_weight'] / 100
    # students' average
    sum_of_all = marks_tests.groupby(['student_id']).sum()
    sum_of_all['student_average'] = (sum_of_all['weighted_marks'] / sum_of_all['test_weight'] * 100).round(2)
    students_average = sum_of_all.drop(labels=['test_id', 'test_mark', 'course_id', 'weighted_marks', 'test_weight'], axis=1).reset_index()
    # students' mark for each course
    sum_per_course = marks_tests.groupby(['student_id', 'course_id']).sum().reset_index()
    sum_per_course = pd.merge(sum_per_course, courses, how='left', on="course_id")
    complete_result = pd.merge(sum_per_course, students, how='left', on="student_id").drop(labels=['test_id', 'test_mark', 'test_weight'], axis=1)
    # final dataframe
    complete_complete = pd.merge(complete_result, students_average, how='left', on="student_id")
    return complete_complete


def csv2json(complete_dataset):
    """
    "csv2json" gets a pandas dataframe of complete records for each student and in return creates a dictionary with the requested format.
        the requested format is:
                    { "students": [   {
                                    "id": 1,
                                    "name": "A",
                                    "totalAverage": 72.03,
                                    "courses": [    {
                                                        "id": 1,
                                                        "name": "Biology",
                                                        "teacher": "Mr. D",
                                                        "courseAverage": 90.1
                                                    } ] } ] }
    :return: a nested dictionary
    """
    results = complete_dataset.to_dict('records')
    final_details = {"students": []}
    records = dict()
    for student in results:
        temp = dict()
        if student['student_id'] not in records.keys():
            temp["id"] = student['student_id']
            temp["name"] = student['student_name']
            temp["totalAverage"] = round(student['student_average'], 2)
            temp['courses'] = [{
                "id": student['course_id'],
                "name": student['course_name'],
                "teacher": student['teacher_name'],
                "courseAverage": round(student['weighted_marks'], 2)
            }]
            records[student['student_id']] = temp
        else:
            records[student['student_id']]['courses'].append({
                "id": student['course_id'],
                "name": student['course_name'],
                "teacher": student['teacher_name'],
                "courseAverage": round(student['weighted_marks'], 2)
            })
    final_details['students'] = list(records.values())
    return final_details
