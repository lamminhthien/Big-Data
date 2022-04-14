#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
from posixpath import split
import sys

current_account = None
current_count = 0
account = None


luot_follows = {}


# lấy dữ liệu tài khoản thiết bị nhập chuẩn
for line in sys.stdin:
    # loại bỏ ký tự trắng ở đầu và cuối chuỗi
    line = line.strip()

    # tách ra thành cặp <b'thien', 1> (Chú ý: Ở file reducer.py cặp <account, 1> xuất ra với ký tự phân cách tab)
    account, count = line.split('\t', 1)

    # chuyển giá trị count thành kiểu số
    try:
        count = int(count)
    except ValueError:
        # nếu không phải giá trị số thì bỏ qua
        continue

    # Ở cuối pha Map, các cặp (key, value) đã được sắp xếp theo key (ở đây là các tài khoản).
    # Vì vậy ở pha Reduce, chương trình sẽ cộng giá trị value của dãy liên tiếp các tài khoản trùng nhau
    # cho đến khi gặp tài khoản mới.
    if account == current_account: # nếu tài khoản mới trùng với tài khoản đang xét thì tăng giá trị đếm của tài khoản đang xét
        # print(account)
        current_count += count
    else:
        if current_account: # nếu gặp tài khoản mới thì in ra số lần xuất hiện của tài khoản đang xét
            luot_follows[current_account] = current_count
        # sau đó chuyển sang xử lý tài khoản mới
        current_count = count
        current_account = account

# in ra tài khoản cuối cùng
if current_account == account:
    # print('%s fuck \t fuck  %s' % (current_account, current_count))
    luot_follows[current_account] = current_count

# Sap Xep Nao
luot_follows_sorted = dict(sorted(luot_follows.items(),key=lambda x:x[1],reverse=True))

# In bang dictonary
for w in list(luot_follows_sorted)[0:20]:
    # print(f'{w} \t {luot_follows_sorted[w]} ')
    print('Tai Khoan %s duoc %s luot theo doi' % (w,luot_follows_sorted[w]))