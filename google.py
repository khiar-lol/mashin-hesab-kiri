import tkinter as tk
import webbrowser

# Function to open Google
def open_google():
    webbrowser.open('https://www.google.com')

# Create the main window
window = tk.Tk()
window.title("Login to Google")
window.geometry("300x150")

# Set background color of the window
window.configure(bg='lightblue')

# Login Label
login_label = tk.Label(window, text="Login with Google", font=('Arial', 14, 'bold'), bg='lightblue')
login_label.pack(pady=10)

# Image frame to hold the logo
frame = tk.Frame(window)
frame.pack(pady=10)




# Login Button
login_button = tk.Button(window, text="Go to Google", command=open_google, bg='green', fg='white', font=('Arial', 12))
login_button.pack(pady=10)

# Start the Tkinter main loop
window.mainloop()