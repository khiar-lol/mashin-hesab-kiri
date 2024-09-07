import tkinter as tk
from tkinter import messagebox
from PIL import Image , ImageTk

# Function to create the login window
def create_login_window():
    window = tk.Tk()
    window.title("لاگین سگ آتیشی")
    window.geometry("500x400")
    window.configure(bg='gray',)
    window.after(201 , lambda:window.iconbitmap(r'fresh_kitchen_eggplant_fruit_icon_261728.ico'))  

    # Load the logo image
    logo_image = Image.open("logo.png")  # Make sure the image is in the same directory
    logo_image = logo_image.resize((100, 100))  # Resize the image
    logo = ImageTk.PhotoImage(logo_image)

    # Create and place the logo
    logo_label = tk.Label(window, image=logo, bg='gray')
    logo_label.image = logo  # Keep a reference to avoid garbage collection
    logo_label.pack(pady=20)

    # Function to check login credentials
    def check_login():
        username = entry_username.get()
        password = entry_password.get()

        # Dummy credentials for demonstration
        if username == "khiar" and password == "54321":
            messagebox.showinfo("🗿آفرین", f"🚪اومدی داخل, {username}!")
        else:
            messagebox.showerror("💩ریدی!!!", "🔫کصکش درست وارد کن")

    # Username Label and Entry
    tk.Label(window, text="اسمت", bg='gray', fg='black' , font=('Arial',18,'bold')).pack(pady=5)
    entry_username = tk.Entry(window , font=('Arial',12) , bg='light gray')
    entry_username.pack(pady=5)

    # Password Label and Entry
    tk.Label(window, text="رمزت", bg='gray', fg='black' , font=('Arial',18,'bold')).pack(pady=5)
    entry_password = tk.Entry(window, show='*' , font=('Arial',12) , bg='light gray')
    entry_password.pack(pady=5)

    # Login Button
    login_button = tk.Button(window, text="اینجارو بمال", command=check_login, bg='gray', fg='black' , font=('Arial',15,'italic'))
    login_button.pack(pady=20)

    window.mainloop()

if __name__ == "__main__":
    create_login_window()