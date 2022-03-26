#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys

current_id = None
follow_count = 1


# Lấy dữ liệu từ thiết bị nhập chuẩn
for line in sys.stdin:
    # Xóa khoảng trắng thừa ở đầu và cuối chuỗi
    line = line.strip()
    # (Chú ý: Ở file reducer.py cặp <id1, id2> xuất ra với ký tự phân cách tab) 
    id1,id2 = line.split('\t',1)
    # Vì cuối pha mapper, các cặp <key,value> đã được sắp xếp thứ tự theo key là id1 nên , ta cộng dồn lượt xuất hiện của các id1 
        # giống nhau đó để thống kê số lượng người theo dõi của mỗi tài khoản
    if current_id == id1:
        follow_count = follow_count + 1
    # Gặp id1 mới thì in ra số lượt follow của tài khoản đó
    else:
        if current_id:
            print(f'User {current_id} follow {follow_count} peoples')
            # Bắt đầu sang xử lý id mới
        current_id = id1
        follow_count = 1

# In số lượng follow của id1 cuối cùng
if current_id == id1:
    print(f'User {current_id} follow {follow_count} peoples')
    
        


