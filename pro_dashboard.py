import pandas as pd
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------- DATA ----------------
data = {
    "Product": ["Coke", "Pepsi", "Juice", "Milk", "Biscuits"],
    "Price": [120, 115, 140, 180, 80],
    "Weight": [500, 500, 1000, 1000, 200],
    "Sugar": [53, 54, 22, 5, 18]
}

df = pd.DataFrame(data)
df["Price_per_100g"] = df["Price"] / df["Weight"] * 100


# ---------------- ANALYTICS ----------------
def best_product():
    return df.loc[df["Price_per_100g"].idxmin()]

def worst_product():
    return df.loc[df["Price_per_100g"].idxmax()]


# ---------------- GUI FUNCTIONS ----------------
def load_table(dataframe):
    for row in table.get_children():
        table.delete(row)

    for _, row in dataframe.iterrows():
        table.insert("", "end", values=list(row))


def show_all():
    load_table(df)
    draw_chart(df)


def show_best():
    best = best_product()
    load_table(pd.DataFrame([best]))
    draw_chart(pd.DataFrame([best]))


def show_worst():
    worst = worst_product()
    load_table(pd.DataFrame([worst]))
    draw_chart(pd.DataFrame([worst]))


def search_product():
    query = search_var.get().lower()
    filtered = df[df["Product"].str.lower().str.contains(query)]
    load_table(filtered)
    draw_chart(filtered)


# ---------------- CHART FUNCTION ----------------
def draw_chart(dataframe):
    ax.clear()

    ax.bar(
        dataframe["Product"],
        dataframe["Price_per_100g"]
    )

    ax.set_title("Price per 100g Comparison", color="white")
    ax.set_ylabel("Price per 100g", color="white")
    ax.set_facecolor("#2b2b3d")

    canvas.draw()


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("🔥 Grocery AI Analytics Dashboard")
root.geometry("1000x600")
root.configure(bg="#1e1e2f")


# ---------------- TOP BAR ----------------
top_frame = tk.Frame(root, bg="#1e1e2f")
top_frame.pack(pady=10)

search_var = tk.StringVar()

tk.Entry(top_frame, textvariable=search_var, width=25).grid(row=0, column=0, padx=5)

tk.Button(top_frame, text="Search", command=search_product, bg="#4CAF50", fg="white").grid(row=0, column=1)
tk.Button(top_frame, text="All", command=show_all, bg="#2196F3", fg="white").grid(row=0, column=2)
tk.Button(top_frame, text="Best", command=show_best, bg="#00C853", fg="white").grid(row=0, column=3)
tk.Button(top_frame, text="Worst", command=show_worst, bg="#D50000", fg="white").grid(row=0, column=4)


# ---------------- TABLE ----------------
frame = tk.Frame(root)
frame.pack(side="left", fill="both", expand=True, padx=10)

columns = list(df.columns)

table = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=120)

table.pack(fill="both", expand=True)


# ---------------- GRAPH AREA ----------------
graph_frame = tk.Frame(root, bg="#1e1e2f")
graph_frame.pack(side="right", fill="both", expand=True)

fig, ax = plt.subplots()
fig.patch.set_facecolor("#1e1e2f")

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(fill="both", expand=True)


# ---------------- START ----------------
show_all()

root.mainloop()
