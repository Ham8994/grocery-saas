import pandas as pd
import tkinter as tk
from tkinter import ttk

# ---------------- DATA ----------------
data = {
    "Product": ["Coke", "Pepsi", "Juice", "Milk", "Biscuits"],
    "Price": [120, 115, 140, 180, 80],
    "Weight": [500, 500, 1000, 1000, 200],
    "Sugar": [53, 54, 22, 5, 18]
}

df = pd.DataFrame(data)
df["Price_per_100g"] = df["Price"] / df["Weight"] * 100

# ---------------- FUNCTIONS ----------------
def show_data():
    text.delete("1.0", tk.END)
    text.insert(tk.END, df.to_string())

def show_best():
    best = df.loc[df["Price_per_100g"].idxmin()]
    text.delete("1.0", tk.END)
    text.insert(tk.END, "BEST VALUE PRODUCT:\n\n")
    text.insert(tk.END, str(best))

def show_worst():
    worst = df.loc[df["Price_per_100g"].idxmax()]
    text.delete("1.0", tk.END)
    text.insert(tk.END, "WORST VALUE PRODUCT:\n\n")
    text.insert(tk.END, str(worst))

# ---------------- GUI WINDOW ----------------
root = tk.Tk()
root.title("Grocery Receipt Detective")
root.geometry("700x500")

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

btn1 = tk.Button(frame, text="Show All Products", command=show_data)
btn1.grid(row=0, column=0, padx=5)

btn2 = tk.Button(frame, text="Best Value", command=show_best)
btn2.grid(row=0, column=1, padx=5)

btn3 = tk.Button(frame, text="Worst Value", command=show_worst)
btn3.grid(row=0, column=2, padx=5)

# Output box
text = tk.Text(root, height=20, width=80)
text.pack(pady=10)

# Start app
root.mainloop()
