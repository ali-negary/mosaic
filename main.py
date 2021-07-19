"""write sth in here
"""

import utils
import sys

if __name__ == '__main__':
    files_list = sys.argv
    # print(files_list)
    students_df = utils.read_file(files_list[2], ['student_id', 'student_name'])
    courses_df = utils.read_file(files_list[1], ['course_id', 'course_name', 'teacher_name'])
    test_df = utils.read_file(files_list[3], ['test_id', 'course_id', 'test_weight'])
    marks_df = utils.read_file(files_list[4], ['test_id', 'student_id', 'test_mark'])
    if utils.check_weights(test_df, marks_df):
        result = utils.calculate_grades(courses=courses_df, students=students_df, tests=test_df, marks=marks_df)
    else:
        result = {"error": "Invalid course weights"}

    utils.save_results(result, files_list[5])
