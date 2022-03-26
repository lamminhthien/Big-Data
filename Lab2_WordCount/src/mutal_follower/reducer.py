#!/usr/bin/python3
"""reducer.py"""
# Thống kê số lượng người theo dõi của mỗi tài khoản
from operator import itemgetter
import sys

# Lấy dữ liệu từ thiết bị nhập chuẩn
for line in sys.stdin:
    # Xóa khoảng trắng thừa ở đầu và cuối chuỗi
    line = line.strip()
    # Tách ra thành cặp id1, id2 
    # (Chú ý: Ở file reducer.py cặp <word, 1> xuất ra với ký tự phân cách tab)


