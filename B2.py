import tkinter as tk
from tkinter import Entry, Label, Button, Text
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_derivative():
    function = function_entry.get()
    x = sp.symbols('x')
    try:
        derivative = sp.diff(function, x)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, str(derivative))
    except:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Lỗi trong việc tính đạo hàm")
# Hàm tính tích phân
def calculate_integral():
    function = function_entry.get()
    x = sp.symbols('x')
    try:
        integral = sp.integrate(function, x)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, str(integral))
    except:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Lỗi trong việc tính tích phân")

# Hàm vẽ đồ thị
def plot_graph():
    function = function_entry.get()
    x = sp.symbols('x')
    try:
        func = sp.lambdify(x, function, 'numpy')
        x_vals = np.linspace(-10, 10, 400)
        y_vals = func(x_vals)
        plt.figure(figsize=(5, 4))
        plt.plot(x_vals, y_vals)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Đồ thị hàm số')
        canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=5, column=0, columnspan=3)
        canvas.draw()
    except:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Lỗi trong việc vẽ đồ thị")

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Ứng dụng môn Giải tích")

# Nhập hàm số
function_label = Label(window, text="Nhập hàm số:")
function_label.grid(row=0, column=0)
function_entry = Entry(window)
function_entry.grid(row=0, column=1)
# Nút tính đạo hàm 
calculate_derivative_button = Button(window, text="Tính đạo hàm", command=calculate_derivative)
calculate_derivative_button.grid(row=1, column=1)

# Nút tính tích phân
calculate_button = Button(window, text="Tính tích phân", command=calculate_integral)
calculate_button.grid(row=1, column=0)

# Kết quả đạo hàm
result_label = Label(window, text="Kết quả đạo hàm:")
result_label.grid(row=2, column=0)
result_text = Text(window, height=5, width=30)
result_text.grid(row=3, column=0, columnspan=3)
# Kết quả tích phân
result_label = Label(window, text="Kết quả tích phân:")
result_label.grid(row=2, column=0)
result_text = Text(window, height=5, width=30)
result_text.grid(row=3, column=0, columnspan=3)

# Nút vẽ đồ thị
plot_button = Button(window, text="Vẽ đồ thị", command=plot_graph)
plot_button.grid(row=4, column=0)

window.mainloop()
