#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys

word_here, word = None # Từ đang xét và từ bình thường (word)
word_count = 0 # Đếm từ

# lấy dữ liệu từ thiết bị nhập chuẩn
for line in sys.stdin:
    # loại bỏ ký tự trắng ở đầu và cuối chuỗi
    line = line.strip()

    # tách ra thành cặp <word, 1> (Chú ý: Ở file reducer.py cặp <word, 1> xuất ra với ký tự phân cách tab)
    word, default_value = line.split('\t', 1)

    # chuyển giá trị default_value thành kiểu số
    try:
        default_value = int(default_value)
    except ValueError:
        # nếu không phải giá trị số thì bỏ qua
        continue

    # Ở cuối pha Map, các cặp (key, value) đã được sắp xếp theo key (ở đây là các từ).
    # Vì vậy ở pha Reduce, chương trình sẽ cộng giá trị value của dãy liên tiếp các từ trùng nhau
    # cho đến khi gặp từ mới.
    if word == word_here: # nếu từ mới trùng với từ đang xét thì tăng giá trị đếm của từ đang xét
        word_count += default_value
    else:
        if word_here: # nếu gặp từ mới thì in ra số lần xuất hiện của từ đang xét
            print('%s\t%s' % (word_here, word_count))
        # sau đó chuyển sang xử lý từ mới
        word_count = default_value
        word_here = word

# in ra từ cuối cùng
if word_here == word:
    print('%s\t%s' % (word_here, word_count))