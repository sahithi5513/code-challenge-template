import mysql.connector
from mysql.connector import Error
from datetime import datetime

DATA_BY_STATION_SQL = '''select WeatherStation, year(yearDate), avg(MaxTemp), avg(MinTemp), sum(AmtOfPrecipitation) from sakila.wx_data group by WeatherStation,year(YearDate)'''
WEATHER_STATION_DATA_SQL = '''select * from sakila.wx_data'''

def create_connection():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='sakila',
                                             user='root',
                                             password='admin')

    except Error as e:
        print("Error while connecting to MySQL", e)
    return connection

def fetchDataByStation():
    result = ''
    try:
        # create a cursor
        with connection.cursor() as cursor:
            cursor.execute(DATA_BY_STATION_SQL)
            result = cursor.fetchall();
            print(result)
    except Error as error:
        print('Error occurred:')
        print(error)
    return result

def fetchAllWeatherData():
    result = ''
    try:
        # create a cursor
        with connection.cursor() as cursor:
            cursor.execute(WEATHER_STATION_DATA_SQL)
            result = cursor.fetchall();
            print(result)
    except Error as error:
        print('Error occurred:')
        print(error)
    return result

connection = create_connection()