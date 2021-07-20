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


# This method calculates the average of students grades.
def calculate_grades(courses, students, tests, marks):
    print("___________________marks_tests________________________")
    marks_tests = pd.merge(marks, tests, how='left', on="test_id")
    # This gives us the weighted marks for each student.
    marks_tests['weighted_marks'] = marks_tests['test_mark'] * marks_tests['test_weight'] / 100
    print(marks_tests)
    print("___________________students_average________________________")
    # This gives us the average of all courses for each student.
    sum_of_all = marks_tests.groupby(['student_id']).sum()
    sum_of_all['student_average'] = (sum_of_all['weighted_marks'] / sum_of_all['test_weight'] * 100).round(2)
    students_average = sum_of_all.drop(labels=['test_id', 'test_mark', 'course_id', 'weighted_marks', 'test_weight'], axis=1).reset_index()
    print(students_average)
    print("_____________________sum_per_course______________________")
    sum_per_course = marks_tests.groupby(['student_id', 'course_id']).sum().reset_index()
    sum_per_course = pd.merge(sum_per_course, courses, how='left', on="course_id")
    complete_result = pd.merge(sum_per_course, students, how='left', on="student_id").drop(labels=['test_id', 'test_mark', 'test_weight'], axis=1)
    print(complete_result)
    print("____________________________complete_complete______________________________")
    complete_complete = pd.merge(complete_result, students_average, how='left', on="student_id")
    print(complete_complete)
    return complete_complete


def csv2json(complete_dataset):
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
    print("________________________________________students_detail_____________________________________")
    print(final_details)

    return final_details
