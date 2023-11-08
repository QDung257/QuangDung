import tkinter as tk
from tkinter import messagebox
import numpy as np
import sympy as sp

# Hàm tính diện tích hình tròn
def calculate_circle_area():
    try:
        radius = float(radius_entry.get())
        if radius < 0:
            messagebox.showerror("Lỗi", "Bán kính không thể là số âm.")
        else:
            area = np.pi * radius ** 2
            result_label.config(text=f"Diện tích hình tròn: {area}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập bán kính hợp lệ.")

# Hàm tính diện tích hình vuông
def calculate_square_area():
    try:
        side = float(side_entry.get())
        if side < 0:
            messagebox.showerror("Lỗi", "Cạnh không thể là số âm.")
        else:
            area = side ** 2
            result_label.config(text=f"Diện tích hình vuông: {area}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập độ dài cạnh hợp lệ.")

# Hàm tính diện tích hình chữ nhật
def calculate_rectangle_area():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        if length < 0 or width < 0:
            messagebox.showerror("Lỗi", "Chiều dài và chiều rộng không thể là số âm.")
        elif length <= width:
            messagebox.showerror("Lỗi", "Chiều dài phải lớn hơn chiều rộng.")
        else:
            area = length * width
            result_label.config(text=f"Diện tích hình chữ nhật: {area}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập chiều dài và chiều rộng hợp lệ.")

# Hàm xóa tất cả dữ liệu
def clear_all():
    radius_entry.delete(0, 'end')
    side_entry.delete(0, 'end')
    length_entry.delete(0, 'end')
    width_entry.delete(0, 'end')
    result_label.config(text="")

# Tạo cửa sổ Tkinter
window = tk.Tk()
window.title("Tính diện tích hình học")

# Tạo các label và entry để nhập thông tin hình tròn
circle_label = tk.Label(window, text="Hình tròn")
radius_label = tk.Label(window, text="Bán kính:")
radius_entry = tk.Entry(window)
circle_label.grid(row=0, column=0)
radius_label.grid(row=1, column=0)
radius_entry.grid(row=1, column=1)

# Tạo các label và entry để nhập thông tin hình vuông
square_label = tk.Label(window, text="Hình vuông")
side_label = tk.Label(window, text="Cạnh:")
side_entry = tk.Entry(window)
square_label.grid(row=2, column=0)
side_label.grid(row=3, column=0)
side_entry.grid(row=3, column=1)

# Tạo các label và entry để nhập thông tin hình chữ nhật
rectangle_label = tk.Label(window, text="Hình chữ nhật")
length_label = tk.Label(window, text="Chiều dài:")
width_label = tk.Label(window, text="Chiều rộng:")
length_entry = tk.Entry(window)
width_entry = tk.Entry(window)
rectangle_label.grid(row=4, column=0)
length_label.grid(row=5, column=0)
width_label.grid(row=6, column=0)
length_entry.grid(row=5, column=1)
width_entry.grid(row=6, column=1)

# Tạo nút tính diện tích và nút xóa
calculate_button = tk.Button(window, text="Tính diện tích", command=lambda: calculate_circle_area() if selected_shape.get() == 1 else calculate_square_area() if selected_shape.get() == 2 else calculate_rectangle_area())
clear_button = tk.Button(window, text="Xóa tất cả", command=clear_all)
calculate_button.grid(row=7, column=0)
clear_button.grid(row=7, column=1)

# Tạo label hiển thị kết quả
result_label = tk.Label(window, text="")
result_label.grid(row=8, column=0, columnspan=2)

# Tạo Radiobutton để chọn hình học
selected_shape = tk.IntVar()
circle_radio = tk.Radiobutton(window, text="Hình tròn", variable=selected_shape, value=1)
square_radio = tk.Radiobutton(window, text="Hình vuông", variable=selected_shape, value=2)
rectangle_radio = tk.Radiobutton(window, text="Hình chữ nhật", variable=selected_shape, value=3)
circle_radio.grid(row=9, column=0)
square_radio.grid(row=9, column=1)
rectangle_radio.grid(row=9, column=2)

# Mặc định chọn hình tròn
selected_shape.set(1)

# Khởi chạy ứng dụng
window.mainloop()
