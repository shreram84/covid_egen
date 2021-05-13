#1. CreateCountyTable.py
This is the one time script which creates tables for all the county regions.

#2. covidDataLoadDaily.py

This script will help to load the data into each of the county for the state of New York

#3. Airflow_scheduler.py

This script will help to schedule the job daily at 9.00am

Assumptions :

1. County in newyork will not change, any new county added should be used to create table

2. Since number of records are lesser we are directly inserting records into each table. If there are more records it would be best to read using pandas by using the copy from which will be used to write data frame into tables.