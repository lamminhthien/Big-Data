#!/usr/bin/python3
"""mapper.py"""

from datetime import datetime
import sys

# Chương trình Python chạy trên Hadoop MapReduce qua tính năng Streaming.
# Dữ liệu vào từ thiết bị nhập chuẩn (STDIN)
# Kết quả xử lý gửi ra thiết bị xuất chuẩn (STDOUT)

for line in sys.stdin.buffer.raw:
    # loại bỏ ký tự trắng ở đầu và cuối chuỗi
    line = line.strip()
    # Bỏ dòng đầu tiên
        # Đang nghĩ cách tối ưu
    # tách ra thành id, created_at và text, chúng được ngăn cách nhau bởi dấu ,
    # print(type(line.split(b',')))
    id,created_at,text = line.split(b',',2)
    # Tùy theo yêu cầu xử lý, ta chọn loại dữ liệu hợp lý để xuất cặp <key,value>
    # ở đây chỉ cần created_at mà thôi, ta sẽ tách ngày và giờ giấc trong từng dòng create_at ra nữa
    # print('%s\t%s' % (text,1))
    # loại bỏ ký tự trắng ở đầu và cuối chuỗi
    date_times = created_at.strip()
    # tách ra thành cặp ngày và giờ giấc
    # dates,times = date_times.split(b' ')
    print('%s\t%s' % (date_times.split(b' ')[-1][0:2],1))
    # đưa ra thiết bị xuất chuẩn các cặp <time, 1>, cách nhau bằng ký tự tab
    # for date_time in date_times.split(b' ')[-1]:
    #     print('%s\t%s' % (date_time, 1))