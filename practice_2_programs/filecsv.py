import csv
# with open('start.csv', 'w') as csvfile:
#     startwriter = csv.writer(csvfile, delimiter=' ',
#                              quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     startwriter.writerow(['Start'] * 2 + ['working example of csv write'])
#     startwriter.writerow(['starting', 'this is an example', 'just a simple working example'])

#
# import csv
#
# newdict = [{'branch': 'ME', 'cgpa': '9.4', 'student_name': 'Sulaksh', 'year': '2'},
#            {'branch': 'COE', 'cgpa': '8.9', 'student_name': 'Amit', 'year': '2'},
#            {'branch': 'IF', 'cgpa': '8.3', 'student_name': 'Rutuja', 'year': '2'},
#            {'branch': 'IM', 'cgpa': '7.1', 'student_name': 'Madhu', 'year': '2'}]
# fields = ['student_name', 'branch', 'year', 'cgpa']
# filename = "uni_records.csv"
# with open('nani3.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#     writer.writeheader()
#     writer.writerows(newdict)


import pandas as pd


def read_csv():
    filepath = "C:\\Users\\venka\Downloads\\50000 Sales Records.csv"
    df = pd.read_csv(filepath)
    return df.head(200).to_string()


print(read_csv())
