#!/usr/bin/python3

import re
import sys

for line in sys.stdin:
  val = line.strip()
  (year, temp, q) = (val[15:19], val[87:92], val[92:93])
  (date) = (val[15:23])
  if (temp != "+9999" and re.match("[01459]", q)):
    print("%s\t%s\t%s" % (year,date,temp))