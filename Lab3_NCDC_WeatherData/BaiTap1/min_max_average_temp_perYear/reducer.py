#!/usr/bin/python3

import sys

sum = 0
count = 0

(last_key, max_val,min_val) = (None, -sys.maxsize,sys.maxsize)
for line in sys.stdin:
  (key, val) = line.strip().split("\t")
  sum = sum + int(val)
  count = count + 1
  if last_key and last_key != key:
    print("%s\t%s\t%s\t%s" % (last_key, max_val, min_val, sum/count))
    (last_key, max_val, min_val) = (key, int(val), int(val))
    sum = 0
    count = 0
  else:
    (last_key, max_val, min_val) = (key, max(max_val, int(val)), min(min_val, int(val)))

if last_key:
  print("%s\t%s\t%s\t%s" % (last_key, max_val, min_val,sum/count))