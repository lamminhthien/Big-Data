from gc import collect
import os, shutil
from pyspark import SparkContext
import re
import sys
sc = SparkContext("local", "Text processing with PySpark Example")

(date_when_max_temperature,max_temperature) = (None,-sys.maxsize)
(current_date, current_year) = (None,None)
lines = sc.textFile("/mnt/c/Big-Data/Lab3_NCDC_WeatherData/data/preprocessed/*.txt").cache()
for line in lines.collect():
    year = line[15:19]
    date = line[15:23]
    temperature = line[87:92]
    q = line[92:93]
    
    if current_year != None and current_year != year:
         print("%s\t%s\t%s" % (current_year, date_when_max_temperature, max_temperature))
         (current_year, max_temperature) = (year, int(temperature))
    else:
        current_year = year
        temperature_integer = int(temperature)
        if (temperature_integer > max_temperature and (temperature != "+9999" and re.match("[01459]",q))):
            max_temperature = temperature_integer
            date_when_max_temperature = date

if current_year:
  print("%s\t%s\t%s" % (current_year, date,max_temperature))
    