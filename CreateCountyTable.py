#!/usr/local/bin/python3
import requests
import json
import sqlite3

request_url = 'https://health.data.ny.gov/api/views/xdss-u53e/rows.json?accessType=DOWNLOAD'


response = requests.get(request_url)
print("Response from api is %s", str(response.status_code))

json_response = response.json()
county_data = None

for column in json_response['meta']['view']['columns']:
    if column['name'] == 'County':
        county_data = column

counties = []



for entry in county_data['cachedContents']['top']:
    counties.append(entry['item'])

print("All counties: ", counties)

connection = sqlite3.connect('/Covid')
cursor = connection.cursor()


for county in counties:
    county = county.replace(" ", "_")
    query = "create table {} (Test_Date Date, New_Positives integer, Cumulative_Number_of_Positives integer,Total_Number_of_Tests_Performed integer,Cumulative_Number_of_Tests_Performed integer,Load_date date)".format(county)
    print(query)
    cursor.execute(query)

