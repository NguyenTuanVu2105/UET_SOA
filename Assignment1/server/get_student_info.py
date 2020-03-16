import csv
import json 

def get_student_info(mssv):
    reader = csv.DictReader(open('student.csv'))
    for row in reader:
        if row['mssv'] == mssv:
            return json.dumps(row, indent=4)
    return

get_student_info(17021138)