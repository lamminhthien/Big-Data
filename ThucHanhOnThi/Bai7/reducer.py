#!/usr/bin/python3

import sys
(current_latitude,current_longtitude) = (None,None)
(last_year, max_temp) = (None, -sys.maxsize)
for line in sys.stdin:
  (year,temp,latitude,longtitude) = line.strip().split("\t")
  if last_year != None and last_year != year:
    print("%s\t%s\t%s\t" % (last_year,int(latitude)/1000,int(longtitude)/1000))
    (last_year, max_temp) = (year, int(temp))
    (current_latitude, current_longtitude) = (latitude,longtitude)
  else:
    last_year = year
    current_temp = int(temp)
    if (current_temp > max_temp):
      max_temp = current_temp
      (current_latitude,current_longtitude) = (latitude,longtitude)

if last_year:
  print("%s\t%s\t%s\t" % (last_year,int(latitude)/1000,int(longtitude)/1000))