#!/usr/bin/python3
'''reducer.py'''

import sys

(last_year, max_temp) = (None, -sys.maxsize)
date_in_max_temp = None
for line in sys.stdin:
  (year,date,temp) = line.strip().split("\t")
  if last_year != None and last_year != year:
    print("%s\t%s" % (last_year, date))
    (last_year, max_temp) = (year, int(temp))
  else:
    # (last_year, max_temp) = (year, max(max_temp, int(temp)))
    last_year = year
    current_temp = int(temp)
    if (current_temp > max_temp):
        max_temp = current_temp
        date_in_max_temp = date
        
    

# In ra kết quả cho năm cuối cùng:
if last_year:
  print("%s\t%s" % (last_year, date))