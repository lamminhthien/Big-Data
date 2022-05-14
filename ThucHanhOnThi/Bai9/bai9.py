from gc import collect
import os, shutil
from pyspark import SparkContext
import re
import sys
sc = SparkContext("local", "Text processing with PySpark Example")

(date_when_max_temp,max_temp) = (None,-sys.maxsize)
(current_date, last_year) = (None,None)
lines = sc.textFile("/mnt/e/HỌC/BT-Bigdata/Big-Data-main/Lab3_NCDC_WeatherData/data/preprocessed/1902.txt").cache()
for line in lines.collect():
    year = line[15:19]
    date = line[15:23]
    temp = line[87:92]
    q = line[92:93]
    
    if last_year != None and last_year != year:
         print("%s\t%s\t%s" % (last_year, date,max_temp))
         (last_year, max_temp) = (year, int(temp))
    else:
        last_year = year
        temp_integer = int(temp)
        if (temp_integer > max_temp and (temp_integer != 9999 and re.match("[01459]",q))):
            max_temp = temp_integer
            date_when_max_temp = date

if last_year:
  print("%s\t%s\t%s" % (last_year, date,max_temp))
    