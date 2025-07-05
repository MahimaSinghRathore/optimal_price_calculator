import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def calculate_optimal_price():
    try:
        a = float(entry_demand.get())  
        b = float(entry_sensitivity.get()) 
        c = float(entry_cost.get())  
        
        price_range = np.linspace(1, 200, 200)

        quantity_sold = a - b * price_range

        revenue = price_range * quantity_sold
        profit = revenue - (c * quantity_sold)

        optimal_price = price_range[np.argmax(profit)]
        max_profit = max(profit)

        label_result.config(
            text=f"Optimal Price: ₹{optimal_price:.2f}\nMaximum Profit: ₹{max_profit:.2f}"
        )

        fig, ax = plt.subplots()
        ax.plot(price_range, profit, label='Profit', color='green')
        ax.scatter(optimal_price, max_profit, color='red') 
        ax.annotate(
            f'Optimal Price\n₹{optimal_price:.2f}',
            xy=(optimal_price, max_profit),
            xytext=(optimal_price + 5, max_profit + 10),
            arrowprops=dict(arrowstyle="->", color='red'),
            color='red'
        )
        ax.set_title("Profit vs. Price")
        ax.set_xlabel("Price")
        ax.set_ylabel("Profit")
        ax.grid(True)

        for widget in frame_plot.winfo_children(): 
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=frame_plot)
        canvas.get_tk_widget().pack()

    except ValueError:
        label_error.config(text="Please enter valid numeric data.")

root = tk.Tk()
root.title("Optimal Price Calculator")

frame_input = ttk.LabelFrame(root, text="Input Data", padding="10")
frame_input.pack(padx=10, pady=10)

ttk.Label(frame_input, text="Base Demand (a):").grid(row=0, column=0, sticky="w")
entry_demand = ttk.Entry(frame_input, width=15)
entry_demand.grid(row=0, column=1)

ttk.Label(frame_input, text="Price Sensitivity (b):").grid(row=1, column=0, sticky="w")
entry_sensitivity = ttk.Entry(frame_input, width=15)
entry_sensitivity.grid(row=1, column=1)

ttk.Label(frame_input, text="Cost per Unit (c):").grid(row=2, column=0, sticky="w")
entry_cost = ttk.Entry(frame_input, width=15)
entry_cost.grid(row=2, column=1)

ttk.Button(frame_input, text="Calculate", command=calculate_optimal_price).grid(row=3, column=0, columnspan=2, pady=5)

frame_plot = ttk.Frame(root)
frame_plot.pack(padx=10, pady=10)

label_result = ttk.Label(root, text="", padding="5")
label_result.pack()

label_error = ttk.Label(root, text="", foreground="red")
label_error.pack()

root.mainloop()