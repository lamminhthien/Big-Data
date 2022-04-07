#!/usr/bin/python3

import sys
current_latitude = None
current_longtitude = None

(last_year, max_temp) = (None, -sys.maxsize)
for line in sys.stdin:
  # (date, time, year, temp, latitude, longtitude))
  (date, time, year, temp, latitude, longtitude) = line.strip().split("\t")
  if last_year != None and last_year != year:
    print("%s\t%s\t%s\t%s\t%s\t%s" % (last_year, max_temp,
          int(latitude)/1000,int(longtitude)/1000,date,time)
        )
    (last_year, max_temp) = (year, int(temp))
    (current_latitude, current_longtitude) = (latitude,longtitude)
  else:
    (last_year, max_temp) = (year, max(max_temp, int(temp)))
    (current_latitude,current_longtitude) = (latitude,longtitude)

if last_year:
  print("%s\t%s\t%s\t%s\t%s\t%s" % (last_year, max_temp,
          int(latitude)/1000,int(longtitude)/1000,date,time)
        )