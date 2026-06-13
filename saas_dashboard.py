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
def load_table(dataframe):
    for row in table.get_children():
        table.delete(row)

    for _, row in dataframe.iterrows():
        table.insert("", "end", values=list(row))


def show_all():
    load_table(df)


def show_best():
    best = df.loc[df["Price_per_100g"].idxmin()]
    load_table(pd.DataFrame([best]))


def show_worst():
    worst = df.loc[df["Price_per_100g"].idxmax()]
    load_table(pd.DataFrame([worst]))


def search_product():
    query = search_var.get().lower()
    filtered = df[df["Product"].str.lower().str.contains(query)]
    load_table(filtered)


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Grocery SaaS Dashboard")
root.geometry("850x500")
root.configure(bg="#1e1e2f")

# Top Frame (Controls)
top_frame = tk.Frame(root, bg="#1e1e2f")
top_frame.pack(pady=10)

search_var = tk.StringVar()

search_entry = tk.Entry(top_frame, textvariable=search_var, width=25)
search_entry.grid(row=0, column=0, padx=5)

search_btn = tk.Button(top_frame, text="Search", command=search_product)
search_btn.grid(row=0, column=1, padx=5)

btn_all = tk.Button(top_frame, text="All Products", command=show_all)
btn_all.grid(row=0, column=2, padx=5)

btn_best = tk.Button(top_frame, text="Best Value", command=show_best)
btn_best.grid(row=0, column=3, padx=5)

btn_worst = tk.Button(top_frame, text="Worst Value", command=show_worst)
btn_worst.grid(row=0, column=4, padx=5)


# Table Frame
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

columns = list(df.columns)

table = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=120)

table.pack(fill="both", expand=True)


# Load default data
show_all()

root.mainloop()
