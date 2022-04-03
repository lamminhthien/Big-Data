#!/usr/bin/python3

import sys

(last_key, max_val,min_val) = (None, -sys.maxsize,sys.maxsize)
for line in sys.stdin:
  sum = 0
  count = 0
  (key, val) = line.strip().split("\t")
  sum = sum + val
  count = count + 1
  if last_key and last_key != key:
    print("%s\t%s\t%s\t%s" % (last_key, max_val, min_val,average_val))
    (last_key, max_val, min_val, average_val) = (key, int(val), int(val))
  else:
    (last_key, max_val, min_val,average_val) = (key, max(max_val, int(val)), min(min_val, int(val)), sum/count)

if last_key:
  print("%s\t%s\t%s\t%s" % (last_key, max_val, min_val,average_val))