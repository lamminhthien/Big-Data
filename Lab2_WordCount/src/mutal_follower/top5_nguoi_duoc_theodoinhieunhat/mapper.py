#!/usr/bin/python3
"""mapper.py"""
import sys


# Đọc từng dòng trong file
for line in sys.stdin.buffer.raw:
    # Xóa khoảng trắng thừa ở đầu và cuối chuỗi
    line = line.strip()
    # tách 2 id ra
    id1,id2 = line.split()
    # in 2 id ra thành từng dòng để cho pha reducer đọc
    print(f'{id2}\t1')


    