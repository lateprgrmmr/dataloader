import MySQLdb

db = MySQLdb.connect(host='localhost', database='scraping_sample', user='scraping_user', password='pword')
c = db.cursor()
# sql = "INSERT INTO classes(name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, created_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})".format(
#     name_of_class, type_of_course, lecturer, number, short_text, choice_term, hours_per_week_in_term, expected_num_of_participants, maximum_participants, assignment, lecture_id, credit_points, hyperlink, language, 'NOW()')
sql = "INSERT INTO classes(name_of_class,hours_per_week_in_term,expected_num_of_participants,maximum_participants,assignment,lecture_id,credit_points,language,created_at) VALUES('test',5,22,30,'test',1,3,'english',NOW())"
#sql = "Select * from classes"
c.execute(sql)
db.commit()
db.close()
#a = c.fetchall()
#print(a)

CREATE TABLE `classes2` (
 `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
 `name_of_class` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `type_of_course` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `lecturer` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `number` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `short_text` text COLLATE utf8_unicode_ci DEFAULT NULL,
 `choice_term` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
 `hours_per_week_in_term` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `expected_num_of_participants` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `maximum_participants` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `assignment` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `lecture_id` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `credit_points` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `hyperlink` text COLLATE utf8_unicode_ci DEFAULT NULL,
 `language` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `created_at` timestamp NULL DEFAULT NULL,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
