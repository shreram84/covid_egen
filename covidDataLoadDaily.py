#!/usr/local/bin/python3
from datetime import datetime
from sqlite3.dbapi2 import Date
import requests
import json
import sqlite3
import argparse

parser = argparse.ArgumentParser(description='Uploads county COVID information')
parser.add_argument('--county', choices=['Monroe','Albany','Bronx','Broome','Cattaraugus','Cayuga','Columbia','Cortland','Erie','Essex','Franklin','Fulton','Herkimer','Livingston','Monroe','New York','Washington','Seneca','Sullivan','Saratoga'],
                    required=True, help='Choose a county to upload')
args = parser.parse_args()
print(args)

request_url = 'https://health.data.ny.gov/api/views/xdss-u53e/rows.json?accessType=DOWNLOAD'


response = requests.get(request_url)
print("Response from api is {}".format(str(response.status_code)))

json_response = response.json()
county_data = json_response['data']
load_date = datetime.now()
date_time = load_date.strftime("%m/%d/%Y")

connection = sqlite3.connect('/Users/shreramsundarrajan/Documents/Covid.sqlite3')
cursor = connection.cursor()

for item in county_data:
    for entry in item:
        if item[9] == args.county:
            table_name = args.county.replace(' ', '_')
            query = "insert into {} (Test_Date, New_Positives,Cumulative_Number_of_Positives,Total_Number_of_Tests_Performed,Cumulative_Number_of_Tests_Performed,Load_date) VALUES ('{}',{},{},{},{},'{}')".format(table_name, item[8],item[10],item[11],item[12],item[13], date_time)
            print(query)
            cursor.execute(query)

cursor.close()
connection.commit()            
print("Finished inserting into table : {}".format(args.county))





