#!/usr/bin/python3
"""mapper.py"""

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
    # ở đây chỉ cần text mà thôi, ta sẽ tách từ trong từng dòng text ra nữa
    # print('%s\t%s' % (text,1))
    # loại bỏ ký tự trắng ở đầu và cuối chuỗi
    text_sequence = text.strip()
    # tách ra thành các từ
    words = text_sequence.split()
    # đưa ra thiết bị xuất chuẩn các cặp <word, 1>, cách nhau bằng ký tự tab
    # Chỉ lấy các từ có chữ @ đầu tiên ví dụ @LamMinhThien
    for word in words:
        if word.decode('ASCII')[0] == b'@'.decode('ASCII'):
            print('%s\t%s' % (word.decode('ASCII'), 1))