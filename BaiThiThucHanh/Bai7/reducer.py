#!/usr/bin/python3

import sys
(current_latitude,current_longtitude) = (None,None)
(current_year, max_temperature) = (None, -sys.maxsize)
for line in sys.stdin:
  ( year, temperature, latitude, longtitude ) = line.strip().split("\t",3)
  if current_year != None and current_year != year:
    print("%s\t%s\t%s\t" % (current_year,int(latitude)/1000,int(longtitude)/1000))
    (current_year, max_temperature) = (year, int(temperature))
    (current_latitude, current_longtitude) = (latitude,longtitude)
  else:
    current_year = year
    current_temp = int(temperature)
    if (current_temp > max_temperature):
      max_temperature = current_temp
      (current_latitude,current_longtitude) = (latitude,longtitude)

if current_year:
  print("%s\t%s\t%s\t" % (current_year,int(latitude)/1000,int(longtitude)/1000))