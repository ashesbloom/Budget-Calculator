import tkinter as tk
from tkinter import messagebox

def calculate_allowance():
    try:
        if all(not day_entry.get().strip() for day_entry in day_entries) and not monthly_entry.get().strip():
            messagebox.showerror("Error", "Please provide either the allowance for weekdays or the monthly allowance.")
            return

        if any(day_entry.get().strip() for day_entry in day_entries):
            weekdays_allowance = sum(float(day_entry.get()) for day_entry in day_entries)
            monthly_allowance = weekdays_allowance * 4
        else:
            monthly_allowance = float(monthly_entry.get())
            weekdays_allowance = monthly_allowance / 4

        weekdays_label.config(text=f"Weekdays Allowance: Rs {weekdays_allowance:.2f}", bg="#233D4D", fg="#FFFFFF")
        monthly_label.config(text=f"Monthly Allowance: Rs {monthly_allowance:.2f}", bg="#233D4D", fg="#FFFFFF")
        root.after(1500, root.destroy)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Allowance Feeder")
root.configure(bg="#D3D0CB")

day_labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_entries = []

for i, day in enumerate(day_labels):
    tk.Label(root, text=day, bg="#D3D0CB", fg="#233D4D").grid(row=i, column=0, padx=5, pady=5, sticky="w")
    tk.Label(root, text="Rs:", bg="#D3D0CB", fg="#233D4D").grid(row=i, column=1, padx=5, pady=5)
    day_entry = tk.Entry(root, bg="#FFFFFF")
    day_entry.grid(row=i, column=2, padx=5, pady=5, sticky="we")
    day_entries.append(day_entry)

tk.Label(root, text="Monthly Allowance:", bg="#D3D0CB", fg="#233D4D").grid(row=7, column=0, padx=5, pady=5, sticky="w")
tk.Label(root, text="Rs:", bg="#D3D0CB", fg="#233D4D").grid(row=7, column=1, padx=5, pady=5)
monthly_entry = tk.Entry(root, bg="#FFFFFF")
monthly_entry.grid(row=7, column=2, padx=5, pady=5, sticky="we")

weekdays_label = tk.Label(root, text="Weekdays Allowance: Rs 0.00", bg="#233D4D", fg="#FFFFFF")
weekdays_label.grid(row=8, column=0, columnspan=3, pady=5, sticky="we")

monthly_label = tk.Label(root, text="Monthly Allowance: Rs 0.00", bg="#233D4D", fg="#FFFFFF")
monthly_label.grid(row=9, column=0, columnspan=3, pady=5, sticky="we")

calculate_button = tk.Button(root, text="Feed", command=lambda: calculate_allowance(), bg="#233D4D", fg="#FFFFFF")
calculate_button.grid(row=10, columnspan=3, pady=10, sticky="we")

for i in range(11):
    root.grid_rowconfigure(i, weight=1)

for j in range(3):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
