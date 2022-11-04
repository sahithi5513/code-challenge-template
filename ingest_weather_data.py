import mysql.connector
from mysql.connector import Error
from datetime import datetime
import csv
from pathlib import Path

def create_connection():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='sakila',
                                             user='root',
                                             password='admin')

    except Error as e:
        print("Error while connecting to MySQL", e)
    return connection

def insert_data(connection,date,maxtemp, mintemp, amtofprecipitation, WeatherStation):
    try:
        # create a cursor
        with connection.cursor() as cursor:
            # execute the insert statement
            c = execute_data(cursor, date, maxtemp, mintemp, amtofprecipitation, WeatherStation)
            print(c)
            print(c.rowcount, "Record inserted successfully into Laptop table")
            c.close()
            # commit work
            connection.commit()
    except Error as error:
        print('Error occurred:')
        print(error)

#construct an insert statement that add a new row to the wx_data Table
def execute_data(cursor, date, max_temp, min_temp, AmtOfPrecipitation, WeatherStation):
    print('Entered in to insert_data')
    sql = '''insert into wx_data(YearDate, MaxTemp, MinTemp, AmtOfPrecipitation, WeatherStation) values(%s, %s, %s, %s, %s)'''
    record = (date, max_temp, min_temp, AmtOfPrecipitation, WeatherStation)
    cursor.execute(sql, record)
    #we can use executemany function for a bulk insert
    return cursor

connection = create_connection()
print(connection)
for p in Path('C:/wx_data').glob('*.csv'):
    print(p)
    with open(p, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            insert_data(connection, row[0], row[1], row[2], row[3], p.name.removesuffix('.csv'))
connection.close()
