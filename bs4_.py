#!/Users/kevinbratt/dataloader/dataload/bin/python3
import requests
from bs4 import BeautifulSoup
import psycopg2
from config import config



#URL to be scraped
url_to_scrape = 'https://howpcrules.com/sample-page-for-web-scraping/'
#Load html's plain data into a variable
plain_html_text = requests.get(url_to_scrape)
#parse the data
soup = BeautifulSoup(plain_html_text.text, "html.parser")
name_of_class = soup.h3.text.strip()

#Get all data associated with this class
basic_data_table = soup.find("table", {"summary": "Basic data for the event"})
#Get all cells in the base data table
basic_data_cells = basic_data_table.findAll('td')

#get all the different data from the table's tds
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
 
# print(soup.prettify())


# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()

#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)

#         # create a cursor
#         cur = conn.cursor()

#         # execute a statement
#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')

#         # display the PostgreSQL database server version
#         #db_version = cur.fetchone()
#         #print(db_version)

#         # close the communication with the PostgreSQL
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')


# if __name__ == '__main__':
#     connect()
