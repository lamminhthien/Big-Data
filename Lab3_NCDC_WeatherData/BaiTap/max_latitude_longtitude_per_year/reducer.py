#!/usr/bin/python3

import sys
current_latitude = None
current_longtitude = None

(last_key, max_val) = (None, -sys.maxsize)
for line in sys.stdin:
  (key,val,latitude,longtitude) = line.strip().split("\t")
  if last_key and last_key != key:
    print("%s\t%s\t%s\t%s" % (last_key, max_val,int(latitude)/1000,int(longtitude)/1000))
    (last_key, max_val) = (key, int(val))
    (current_latitude, current_longtitude) = (latitude,longtitude)
  else:
    (last_key, max_val) = (key, max(max_val, int(val)))
    (current_latitude,current_longtitude) = (latitude,longtitude)

if last_key:
  print("%s\t%s\t%s\t%s" % (last_key, max_val,int(latitude)/1000,int(longtitude)/1000))