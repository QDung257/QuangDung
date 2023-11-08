import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox

# Hàm xử lý khi người dùng chọn ảnh từ bàn phím
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        image = cv2.imread(file_path)
        if image is not None:
            edge_image = get_edge_image(image)
            cv2.imshow("Anh goc", image)
            cv2.imshow("Tach bien", edge_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            messagebox.showerror("Error", "Không thể đọc ảnh. Vui lòng chọn một tập tin hình ảnh hợp lệ.")

# Hàm xử lý để tách biên ảnh
def get_edge_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edge_image = cv2.Canny(blurred, 50, 150)
    return edge_image

# Tạo giao diện người dùng sử dụng Tkinter
root = tk.Tk()
root.title("Tách biên ảnh")
root.geometry('450x450')
select_button = tk.Button(root, text="Chọn ảnh", command=select_image)
select_button.pack()

root.mainloop()
