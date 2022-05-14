#!/usr/bin/python3

import sys

sum = 0
count = 0

last_key = None
for line in sys.stdin:
  (key, val) = line.strip().split("\t")
  sum = sum + int(val)
  count = count + 1
  if last_key and last_key != key:
    print(f"{last_key}\t{round(sum/count)}")
    last_key = key
    sum = 0
    count = 0
  else:
    last_key = key

if last_key:
  print(f"{last_key}\t{round(sum/count)}")