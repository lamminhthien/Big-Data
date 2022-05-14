#!/usr/bin/python3
'''reducer.py'''

import sys

# Khởi tạo giá trị năm, nhiệt độ
( current_year,  min_temperature ) = ( None,  sys.maxsize)
for line in sys.stdin:
  # Lấy cặp giá trị <k, v> = <year, temperature> từ stdin
  ( year,  temperature ) = line.strip().split("\t")
  # Nếu năm đọc vào khác năm đang xét -> (1) đưa ra stdout năm trước đó cùng với nhiệt độ cao nhất
  if current_year != None and current_year != year:
    print("%s\t%s" % ( current_year,  min_temperature ))
    # và (2) chuyển <năm, nhiệt độ> đọc vào thành <năm, nhiệt độ> đang xét:
    ( current_year,  min_temperature ) = ( year,  int(temperature) )
  else:
    # Nếu năm đọc vào trùng với năm đang xét -> tìm nhiệt độ lớn nhất của năm đó:
     (current_year,  min_temperature ) = ( year,  min( min_temperature,  int(temperature) ) )

# In ra kết quả cho năm cuối cùng:
if current_year:
  print("%s\t%s" % (current_year, min_temperature))