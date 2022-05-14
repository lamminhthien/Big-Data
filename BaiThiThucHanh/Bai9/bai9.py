from pyspark import SparkContext
import re
import sys
sc = SparkContext("local", "Text processing with PySpark Example")

max_temperature = -sys.maxsize
current_year = None
lines = sc.textFile("/mnt/c/Big-Data/Lab3_NCDC_WeatherData/data/preprocessed/*.txt").cache()
for line in lines.collect():
    year = line[15:19]
    temperature = line[87:92]
    q = line[92:93]
    
    if current_year != None and current_year != year:
         print("%s\t%s" % (current_year, max_temperature))
         (current_year, max_temperature) = (year, int(temperature))
    else:
        current_year = year
        if (temperature != "+9999" and re.match("[01459]", q)):
            max_temperature = max(int(temperature),max_temperature)

if current_year:
  print("%s\t%s" % (current_year,max_temperature))
    