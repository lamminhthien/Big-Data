# Sys để đọc dữ liệu từ terminal
import sys
# Tạo array mô phỏng lại quá trình shuffing bên hadoop
shuffing_emulator = []
# Đọc output được tạo ra từ file mapper.py và đưa vào mảng để chuẩn bị shuffing
for line in sys.stdin:
    shuffing_emulator.append(line)
    # print(line)
# Bắt đầu shuffing
for element in sorted(shuffing_emulator):
    print(element, sep=' ', end='', flush=True)
