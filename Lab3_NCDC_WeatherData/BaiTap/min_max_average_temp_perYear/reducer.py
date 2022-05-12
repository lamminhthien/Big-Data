#!/usr/bin/python3

import sys

# Biến sum: tính tổng tất cả nhiệt độ đo được trong năm
# Biến count: số lần đo nhiệt độ trong năm
sum = 0
count = 0

(last_key, max_val,min_val) = (None, -sys.maxsize,sys.maxsize)
for line in sys.stdin:
  (key, val) = line.strip().split("\t")
  # Cộng dồn nhiệt độ ở mỗi lần đo được
  sum = sum + int(val)
  # Tăng biến đếm số lần đo được lên
  count = count + 1
  if last_key and last_key != key:
    #print("%s_%s_%s_%s" % (last_key, max_val, min_val, round(sum/count)))
    print(f"{last_key}\t{max_val}\t{min_val}\t{round(sum/count)}")
    (last_key, max_val, min_val) = (key, int(val), int(val))
    sum = 0
    count = 0
  else:
    (last_key, max_val, min_val) = (key, max(max_val, int(val)), min(min_val, int(val)))

if last_key:
  # Ta lấy sum/count ra nhiệt độ trung bình
  print(f"{last_key}\t{max_val}\t{min_val}\t{round(sum/count)}")