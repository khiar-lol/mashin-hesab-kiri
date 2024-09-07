import tkinter as tk

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = eval(expression)
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

# Function to add a character to the entry field
def add_to_expression(char):
    current_text = entry_var.get()
    entry_var.set(current_text + str(char))

# Function to clear the entry field
def clear_expression():
    entry_var.set("")

# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x600")
window.configure(bg='lightgray')

# Variable to store the current expression
entry_var = tk.StringVar()

# Create the entry field
entry = tk.Entry(window, textvariable=entry_var, font=('Arial', 24), justify='right', bd=10, bg='white')
entry.pack(fill='both', padx=10, pady=10)

# Create buttons for the calculator
buttons_frame = tk.Frame(window)
buttons_frame.pack()

# List of button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place buttons in the grid
row, col = 0, 0
for button in buttons:
    if button == 'C':
        btn = tk.Button(buttons_frame, text=button, font=('Arial', 18), command=clear_expression, bg='red', fg='white')
    elif button == '=':
        btn = tk.Button(buttons_frame, text=button, font=('Arial', 18), command=lambda: evaluate_expression(entry_var.get()), bg='green', fg='white')
    else:
        btn = tk.Button(buttons_frame, text=button, font=('Arial', 18), command=lambda char=button: add_to_expression(char), bg='lightblue')

    btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

    col += 1
    if col > 3:  # Move to the next row after 4 buttons
        col = 0
        row += 1

# Configure the grid
for i in range(4):
    buttons_frame.columnconfigure(i, weight=1)
for i in range(4):
    buttons_frame.rowconfigure(i, weight=1)

# Start the Tkinter main loop
window.mainloop()
