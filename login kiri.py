import tkinter as tk
from tkinter import messagebox

# ایجاد پنجره اصلی
def create_login_window():
    window = tk.Tk()
    window.title("صفحه لاگین کیری")

    # دیکشنری کاربران
    users = {
        "user1": "password1",
        "user2": "password2"
    }

    # تابع برای بررسی ورود
    def check_login():
        username = entry_username.get()
        password = entry_password.get()

        if username in users and users[username] == password:
            messagebox.showinfo("ورود موفق", f"خوش آمدید، {username}!")
        else:
            messagebox.showerror("خطا", "اسم یا رمز کیریت خرابه")

    # تنظیمات لایه‌بندی
    tk.Label(window, text="نام کیری :").grid(row=0, column=0, padx=10, pady=10)
    entry_username = tk.Entry(window)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(window, text="رمز کیری :").grid(row=1, column=0, padx=10, pady=10)
    entry_password = tk.Entry(window, show='*')
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    # دکمه ورود
    login_button = tk.Button(window, text="کص ننت اگه اینو بزنی", command=check_login)
    login_button.grid(row=2, columnspan=2, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_login_window()