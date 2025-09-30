import tkinter as tk
from tkinter import messagebox, simpledialog

# -----------------------------
# Backend Data
# -----------------------------
menu = {
    1: ("Idly", 30),
    2: ("Dosa", 50),
    3: ("Poori", 40),
    4: ("Biryani", 120),
    5: ("CoolDrink", 20),
    6: ("Pizza", 90)
}
orders = []

# -----------------------------
# Backend Functions
# -----------------------------
def show_menu():
    items = "\n".join([f"{num}. {dish} : ₹{price}" for num, (dish, price) in menu.items()])
    messagebox.showinfo("Menu", items)

def take_order():
    try:
        dish_num = simpledialog.askinteger("Order", "Enter dish number:")
        if dish_num in menu:
            dish, price = menu[dish_num]
            qty = simpledialog.askinteger("Quantity", f"Enter quantity for {dish}:")
            if  qty > 0:
                if(qty==1):
                   orders.append({"dish": dish, "qty": qty, "price": price * qty})
                   messagebox.showinfo("Success", f"{qty} {dish} added to order!")
                if(qty>1):
                	orders.append({"dish": dish,"qty":qty, "price":price*qty})
                	messagebox.showinfo("Success", f"{qty} {dish}'S added to order!")
            else:
                messagebox.showerror("Error", "Invalid quantity!")
        else:
            messagebox.showerror("Error", "Invalid dish number!")
    except Exception:
        messagebox.showerror("Error", "Something went wrong!")

def show_orders():
    if not orders:
        messagebox.showinfo("Orders", "No items ordered yet.")
        return
    text = "\n".join([f"{o['qty']} x {o['dish']} = ₹{o['price']}" for o in orders])
    messagebox.showinfo("Current Orders", text)

def generate_bill():
    if not orders:
        messagebox.showinfo("Bill", "No orders placed yet.")
        return
    text = "\n".join([f"{o['qty']} x {o['dish']} = ₹{o['price']}" for o in orders])
    total = sum(o['price'] for o in orders)
    text += f"\n\nTotal Amount = ₹{total}\n\nThank You! Visit Again 🍴"
    messagebox.showinfo("Final Bill", text)

# -----------------------------
# Tkinter GUI
# -----------------------------
def main_app():
    app = tk.Tk()
    app.title("Restaurant Management System")
    app.geometry("450x350")
    
    tk.Label(app, text="🍽️ Welcome to Simhadri Restaurant 🍴", font=("Arial", 16), fg="blue").pack(pady=20)
    
    tk.Button(app, text="Show Menu", font=("Arial", 12), width=20, bg="lightgreen", command=show_menu).pack(pady=5)
    tk.Button(app, text="Take Order", font=("Arial", 12), width=20, bg="lightyellow", command=take_order).pack(pady=5)
    tk.Button(app, text="Show Orders", font=("Arial", 12), width=20, bg="lightblue", command=show_orders).pack(pady=5)
    tk.Button(app, text="Generate Bill", font=("Arial", 12), width=20, bg="orange", command=generate_bill).pack(pady=5)
    tk.Button(app, text="Exit", font=("Arial", 12), width=20, bg="red", command=app.destroy).pack(pady=20)
    
    app.mainloop()

# -----------------------------
# Welcome Screen
# -----------------------------
def welcome_screen():
    root = tk.Tk()
    root.title("Welcome")
    root.geometry("400x200")
    tk.Label(root, text="🍽️ Welcome to Simhadri Restaurant 🍴", font=("Arial", 16), fg="green").pack(pady=40)
    tk.Button(root, text="Enter", font=("Arial", 12), width=15, command=lambda:[root.destroy(), main_app()]).pack()
    root.mainloop()

# -----------------------------
# Run the App
# -----------------------------
welcome_screen()
