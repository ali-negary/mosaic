"""This program is a part of interview process for MOSAIC.
    by Ali Negary

    - To run this program, one needs to use the CLI. The command should be in the following manner:
        python main.py courses.csv students.csv tests.csv marks.csv output.json
        courses.csv indicates the location of "courses.csv" file if the file and program are in the same place.
        Otherwise the location must be specified clearly.
"""

import utils
import sys

if __name__ == '__main__':
    files_list = sys.argv
    # Lines 14-17 get the .csv files and replace their headers with the provided the headers.
    students_df = utils.read_file(files_list[2], ['student_id', 'student_name'])
    courses_df = utils.read_file(files_list[1], ['course_id', 'course_name', 'teacher_name'])
    test_df = utils.read_file(files_list[3], ['test_id', 'course_id', 'test_weight'])
    marks_df = utils.read_file(files_list[4], ['test_id', 'student_id', 'test_mark'])

    # The if condition checks if the summation of the marks in one course adds up to 100 or not.
    if utils.check_weights(test_df, marks_df):
        # Required calculations will be provided as a pandas dataframe in the next line.
        info_and_grades = utils.calculate_grades(courses=courses_df, students=students_df, tests=test_df, marks=marks_df)
        # Dataframe of the result "info_and_grades" will be converted to a dictionary in the specified format.
        result = utils.csv2json(info_and_grades)
    else:
        # In case the condition is not met, the following error message must be sent to output.
        result = {"error": "Invalid course weights"}

    # Final step is saving the dictionary on the disk in JSON format.
    utils.save_results(result, files_list[5])
