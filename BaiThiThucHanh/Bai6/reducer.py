#!/usr/bin/python3
'''reducer.py'''

import sys

(current_year, max_temperature) = ( None, -sys.maxsize )
date_have_max_temperature = None
for line in sys.stdin:
  (year,date,temperature) = line.strip().split("\t")
  if current_year != None and current_year != year:
    print("%s\t Ngay %s Thang %s" % (current_year,date_have_max_temperature[6:8],date_have_max_temperature[4:6]))
    (current_year, max_temperature) = (year, int(temperature))
    date_have_max_temperature = date
  else:
    # (current_year, max_temperature) = (year, max(max_temperature, int(temperature)))
    current_year = year
    current_temp = int(temperature)
    if (current_temp > max_temperature):
        max_temperature = current_temp
        date_have_max_temperature = date
        
    

# In ra kết quả cho năm cuối cùng:
if current_year:
  print("%s\t Ngay %s Thang %s" % (current_year,date_have_max_temperature[6:8],date_have_max_temperature[4:6]))