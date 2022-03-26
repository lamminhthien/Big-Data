#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys


# Chứa các cặp theo dõi lẫn nhau
mutual_followers = []
# Chứa tất cả cặp theo dõi
pair_followers = []



# Lấy dữ liệu từ thiết bị nhập chuẩn
for line in sys.stdin:
    # Xóa khoảng trắng thừa ở đầu và cuối chuỗi
    line = line.strip()
    # (Chú ý: Ở file reducer.py cặp <id1, id2> xuất ra với ký tự phân cách tab) 
    id1,id2 = line.split('\t',1)
    # Vì cuối pha mapper, các cặp <key,value> đã được sắp xếp thứ tự theo key là id1 nên
    pair_followers.append((id1,id2))
    # Từ cặp thứ hai trở đi, ta sẽ kiểm tra xem cặp tài khoản đó có phải là mutal follower hay không
    if len(pair_followers) != 0:
        # Nếu (id2,id1) hiện tại khớp với bất kì (id1,id2) nào trong pair_followers thì ta thêm vào mutual_followers
        if (id2,id1) in pair_followers:
            mutual_followers.append((id2,id1))
    


