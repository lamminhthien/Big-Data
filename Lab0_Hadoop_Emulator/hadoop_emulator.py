# Sys để đọc dữ liệu từ terminal
import sys
# Tạo array mô phỏng lại quá trình shuffing bên hadoop
shuffing_emulator = []
# Đọc output được tạo ra từ file mapper.py
for line in sys.stdin:
    shuffing_emulator.append(line)
    # print(line)
print(sorted(shuffing_emulator))