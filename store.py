import tkinter as tk
from tkinter import ttk

class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, code, name, price):
        if code not in self.products:
            self.products[code] = Product(code, name, price)
            print(f"Product with code {code} added to inventory.")
        else:
            print(f"Product with code {code} already exists.")

    def update_product_price(self, code, new_price):
        if code in self.products:
            self.products[code].price = new_price
            print(f"Price of product with code {code} updated to {new_price}.")
        else:
            print(f"Product with code {code} does not exist.")

class InventoryApp:
    def __init__(self, root):
        self.inventory = Inventory()
        self.root = root
        self.root.title("Inventory Management")

        # UI Elements
        ttk.Label(root, text="Code:").grid(column=0, row=0)
        self.code_entry = tk.Entry(root , bg='light gray' , fg='black')
        self.code_entry.grid(column=1, row=0)

        ttk.Label(root, text="Name:").grid(column=0, row=1)
        self.name_entry = tk.Entry(root , bg='light gray' , fg='black')
        self.name_entry.grid(column=1, row=1)

        ttk.Label(root, text="Price:").grid(column=0, row=2)
        self.price_entry = tk.Entry(root , bg='light gray' , fg='black')
        self.price_entry.grid(column=1, row=2)

        add_button = ttk.Button(root, text="Add Product", command=self.add_product)
        add_button.grid(column=1, row=3)

        update_button = ttk.Button(root, text="Update Price", command=self.update_product_price)
        update_button.grid(column=1, row=4)

        self.clear_entries()

    def add_product(self):
        code = self.code_entry.get()
        name = self.name_entry.get()
        price = self.price_entry.get()
        if code and name and price:
            try:
                price = int(price)
                self.inventory.add_product(code, name, price)
                self.clear_entries()
            except ValueError:
                print("Please enter a valid integer for price.")

    def update_product_price(self):
        code = self.code_entry.get()
        new_price = self.price_entry.get()
        if code and new_price:
            try:
                new_price = int(new_price)
                self.inventory.update_product_price(code, new_price)
                self.clear_entries()
            except ValueError:
                print("Please enter a valid integer for price.")

    def clear_entries(self):
        self.code_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

root = tk.Tk()
app = InventoryApp(root)
root.mainloop()