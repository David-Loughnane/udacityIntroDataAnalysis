import unicodecsv
from datetime import datetime as dt

# option 1 : each row is a list
# csv = [['a1', 'a2', 'a3'], ['b1','b2','b3']]

# option 2 : each row is a dictionary, good if you have headers
# csv = [{'name1':'a1', 'name2':'a2', 'name2':'a3'}, {'name1':'b1', 'name2':'b2', 'name2':'b3'}]


def read_csv(filename):
	with open(filename, 'rb') as f:
		reader = unicodecsv.DictReader(f)
		return list(reader)

def parse_date(date):
	if date == '':
		return None
	else:
		return dt.strptime(date, '%Y-%m-%d')

def parse_maybe_int(i):
	if i == '':
		return None
	else:
		return int(i)

enrollments = read_csv('enrollments.csv')
print(enrollments[0])
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

# update types from string
for enrollment in enrollments:
	enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
	enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
	enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
	enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
	enrollment['join_date'] = parse_date(enrollment['join_date'])

for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])


print(len(enrollments))
unique_enrolled_students = set()
for enrollment in enrollments:
    unique_enrolled_students.add(enrollment['account_key'])
print(len(unique_enrolled_students))

print(len(daily_engagement))
unique_engagement_students = set()
for engagement_record in daily_engagement:
    unique_engagement_students.add(engagement_record['acct'])
print(len(unique_engagement_students))

print(len(project_submissions))
unique_project_submitters = set()
for submission in project_submissions:
    unique_project_submitters.add(submission['account_key'])
print(len(unique_project_submitters))