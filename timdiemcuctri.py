import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import math

# Hàm kiểm tra tính hợp lệ của biểu thức hàm số
def is_expression_valid(expression):
    try:
        x = 0
        y = eval(expression)
        return True
    except:
        return False

# Hàm vẽ đồ thị
def draw_graph():
    # Xóa đồ thị cũ (nếu có)
    plt.clf()

    # Lấy biểu thức từ ô văn bản
    expression = expression_entry.get()

    # Kiểm tra tính hợp lệ của biểu thức
    if not is_expression_valid(expression):
        error_label.config(text='Lỗi: Biểu thức không hợp lệ')
        return

    # Lấy miền xác định từ ô văn bản
    domain = domain_entry.get()
    domain = [float(x.strip()) for x in domain.split(',')]

    # Miền xác định
    x = np.linspace(domain[0], domain[1], 100)

    # Tính giá trị của hàm số trên miền xác định
    y = eval(expression)

    # Tìm giá trị tối thiểu và tối đa
    min_value = np.min(y)
    max_value = np.max(y)

    # Vẽ đồ thị đường của hàm số
    plt.plot(x, y, label='f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Đồ thị của hàm số')

    # Tìm điểm cực trị
    min_index = np.argmin(y)
    max_index = np.argmax(y)

    # Vẽ các điểm cực trị
    plt.scatter(x[min_index], y[min_index], c='red', label=f'Minimum ({x[min_index]:.2f}, {y[min_index]:.2f})')
    plt.scatter(x[max_index], y[max_index], c='blue', label=f'Maximum ({x[max_index]:.2f}, {y[max_index]:.2f})')

    plt.legend()

    # Xóa cảnh báo lỗi nếu có
    error_label.config(text='')

    # Hiển thị thông tin hàm số và điểm cực trị trong giao diện
    function_info.config(text=f'Hàm số: {expression}')
    max_value_info.config(text=f'Giá trị Max: {max_value:.2f} (tại x = {x[max_index]:.2f})')
    min_value_info.config(text=f'Giá trị Min: {min_value:.2f} (tại x = {x[min_index]:.2f})')

    plt.show()

# Tạo cửa sổ ứng dụng
window = tk.Tk()
window.title('Tìm cực trị của hàm số')

# Khung chứa phần nhập liệu
input_frame = tk.Frame(window)
input_frame.pack(pady=10)

# Label và textbox cho biểu thức hàm số
expression_label = tk.Label(input_frame, text='Hàm số f(x):')
expression_label.grid(row=0, column=0, padx=10)
expression_entry = tk.Entry(input_frame)
expression_entry.grid(row=0, column=1, padx=10)

# Label và textbox cho miền xác định
domain_label = tk.Label(input_frame, text='Miền xác định (a, b):')
domain_label.grid(row=1, column=0, padx=10)
domain_entry = tk.Entry(input_frame)
domain_entry.grid(row=1, column=1, padx=10)

# Nút vẽ đồ thị
draw_button = tk.Button(input_frame, text='Vẽ đồ thị', command=draw_graph)
draw_button.grid(row=0, column=2, padx=10)

# Khung chứa phần hiển thị thông tin
info_frame = tk.Frame(window)
info_frame.pack(pady=10)

# Nhãn hiển thị thông tin hàm số
function_info = tk.Label(info_frame, text='', font=('Arial', 12))
function_info.pack()

# Nhãn hiển thị giá trị Max
max_value_info = tk.Label(info_frame, text='', font=('Arial', 12))
max_value_info.pack()

# Nhãn hiển thị giá trị Min
min_value_info = tk.Label(info_frame, text='', font=('Arial', 12))
min_value_info.pack()


error_label = tk.Label(info_frame, text='', font=('Arial', 12), fg='red')
error_label.pack()
# Khởi chạy ứng dụng
window.mainloop()
