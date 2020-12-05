import requests
import MySQLdb
from bs4 import BeautifulSoup

# SQL connection
# HOST = 'localhost'
# USERNAME = 'scraping_user'
# PASSWORD = 'pword'
# DATABASE = 'scraping_sample'

# URL
url_to_scrape = 'https://howpcrules.com/sample-page-for-web-scraping/'
plain_html_text = requests.get(url_to_scrape)
soup = BeautifulSoup(plain_html_text.text, 'html.parser')
# print(soup.prettify())

name_of_class = soup.h3.text.strip()
print(name_of_class)

basic_data_table = soup.find('table', {'summary': 'Basic data for the event'})
basic_data_cells = basic_data_table.findAll('td')

# get all the different data from the table's tds
type_of_course = basic_data_cells[0].text.strip()
lecturer = basic_data_cells[1].text.strip()
number = basic_data_cells[2].text.strip()
short_text = basic_data_cells[3].text.strip()
choice_term = basic_data_cells[4].text.strip()
hours_per_week_in_term = basic_data_cells[5].text.strip()
expected_num_of_participants = basic_data_cells[6].text.strip()
maximum_participants = basic_data_cells[7].text.strip()
assignment = basic_data_cells[8].text.strip()
lecture_id = basic_data_cells[9].text.strip()
credit_points = basic_data_cells[10].text.strip()
hyperlink = basic_data_cells[11].text.strip()
language = basic_data_cells[12].text.strip()

db = MySQLdb.connect(host='localhost', database='scraping_sample', user='scraping_user', password='pword')
# print('anus')
cursor = db.cursor()
# print('gum')
sql = "INSERT INTO classes(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(
    name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, 'NOW()')
# print(sql)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
sql = "SELECT LAST_INSERT_ID()"
try:
    cursor.execute(sql)
    result = cursor.fetchone()
    class_id = result[0]
except:
    db.rollback()
    db.close()
    class_id = -1

dates_tables = soup.find_all(
    'table', {'summary': 'Overview of all event dates'})
for table in dates_tables:
    for row in table.select('tr'):
        cells = row.findAll('td')
        if (len(cells) > 0):
            duration = cells[0].text.split('to')
            start_date = duration[0].strip()
            end_date = duration[1].strip()
            day = cells[1].text.strip()
            time = cells[2].text.strip('to')
            start_time = time[0].strip()
            end_time = time[1].strip()
            frequency = cells[3].text.strip()
            room = cells[4].text.strip()
            lecturer_for_date = cells[5].text.strip()
            status = cells[6].text.strip()
            remarks = cells[7].text.strip()
            cancelled_on = cells[8].text.strip()
            max_participants = cells[9].text.strip()

            db = MySQLdb.connect(host='localhost', database='scraping_sample', user='scraping_user', password='pword')
            cursor = db.cursor()
            sql = "INSERT INTO events(class_id, start_date, end_date, day, start_time, end_time, frequency, room, lecturer_for_date, status, remarks, cancelled_on, max_participants, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(
                class_id, start_date, end_date, day, start_time, end_time, frequency, room, lecturer_for_date, status, remarks, cancelled_on, max_participants, 'NOW()')
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
                db.close()
