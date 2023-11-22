import numpy as np
import matplotlib.pyplot as plt

def moving_average_filter(signal, window_size):
    filter_coeffs = np.ones(window_size) / window_size
    filtered_signal = np.convolve(signal, filter_coeffs, mode='valid')
    return filtered_signal

# Nhập tín hiệu từ người dùng
input_signal = input("Nhập tín hiệu (các giá trị cách nhau bằng khoảng trắng): ")
signal = np.array(list(map(float, input_signal.split())))

# Nhập kích thước cửa sổ của bộ lọc từ người dùng
window_size = int(input("Nhập kích thước cửa sổ của bộ lọc: "))

# Áp dụng bộ lọc trung bình
filtered_signal = moving_average_filter(signal, window_size)

# Vẽ biểu đồ tín hiệu gốc và tín hiệu đã lọc
plt.figure(figsize=(10, 6))
plt.plot(signal, label='Tín hiệu gốc')
plt.plot(filtered_signal, label='Tín hiệu đã lọc', linestyle='--')
plt.xlabel('Mẫu')
plt.ylabel('Giá trị')
plt.title('Bộ lọc trung bình đơn giản')
plt.legend()
plt.grid(True)
plt.show()
