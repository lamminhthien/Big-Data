#!/usr/bin/python3

import sys
current_latitude = None
current_longtitude = None

(last_year, max_temp) = (None, -sys.maxsize)
# Ví dụ ban đầu ta có nhiệt độ là 180 độ, ta muốn so sánh được, ta sẽ so sánh với số cực kì nhỏ nhất
# -sys.maxsize
# Đọc dữ liệu có từ file mapper (stdin system input)
for line in sys.stdin:
  # (date, time, year, temp, latitude, longtitude))
  (date, time, year, temp, latitude, longtitude) = line.strip().split("\t")
  if last_year != None and last_year != year:
    print("%s\t%s\t%s\t%s\t%s\t%s" % (last_year, max_temp,
          int(latitude)/1000,int(longtitude)/1000,date,time)
        )
    (last_year, max_temp) = (year, int(temp))
    (current_latitude, current_longtitude) = (latitude,longtitude)
    # Vòng lặp đầu tiên chưa có dữ liệu gì, nó sẽ chạy else trước
  else:
    (last_year, max_temp) = (year, max(max_temp, int(temp)))
    # (1930,180) max_temp = 180 
    # (1930,max(180,185))  => (1930,185)  max_temp = 185
    (current_latitude,current_longtitude) = (latitude,longtitude)

if last_year:
  print("%s\t%s\t%s\t%s\t%s\t%s" % (last_year, max_temp,
          int(latitude)/1000,int(longtitude)/1000,date,time)
        )