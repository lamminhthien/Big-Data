#!/usr/bin/python3

import re
import sys

# Xét từng dòng trong system input (input của terminal)
for line in sys.stdin:
  # Strip là loại bỏ khoảng trắng thừa
  val = line.strip()
  
  # Tạo một bô  ba dữ liệu về năm,nhiệt độ, q (ko biết)
  # year là kí tự thứ 15 đến 19 trong 1 dòng
  # temp là ... 87 đến 92
  (year, temp, q) = (val[15:19], val[87:92], val[92:93])
  (latitude,longtitude) = (val[28:34],val[34:41])
  (date,time) = (val[15:23],val[23:27])
  if (temp != "+9999" and re.match("[01459]", q)):
    # 6 %s tương đường 6 cái trong ngoặc (date, time, year, temp, latitude, longtitude)
    print("%s\t%s\t%s\t%s\t%s\t%s" % (date, time, year, temp, latitude, longtitude))


# CÁch test
# cat /mnt/d/Code/Big-Data/Lab3_NCDC_WeatherData/data/preprocessed/*.txt đuôi *.txt là lấy tất cả
# file txt để làm (system input) cho lệnh for line in sys.stdin(system input):
# Dấu | là chuyển dữ liệu stdin (system input) sang file mapper.py
# ta sẽ thực thi file mapper.py sau dấu |
# chạy ok là file mapper không bị lỗi
# test file mapper xong sẽ qua reduce