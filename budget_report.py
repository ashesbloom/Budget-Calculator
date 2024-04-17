from datetime import datetime, timedelta
import calendar
import time
# Allowance for each day of the week

allowance = {'Monday': 30, 'Tuesday': 30, 'Wednesday': 30, 'Thursday': 30, 'Friday': 30, 'Saturday': 50,
             'Sunday': 100}
monthly_allowance = 1500  # monthly allowance

print("allowance:", allowance)
print("monthly allowance:", monthly_allowance)

# ANSI escape codes for colors
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'  # Reset color to default

# Function to animate the welcome message
def animate_string(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.015)  # Adjust the delay here for animation speed
    print()


# Define the string with color
welcome_msg = f"\n\t{GREEN}Welcome to the{BLUE} budget {YELLOW}calculator{RESET}\n"

animate_string(welcome_msg)

budget = sorted(allowance.values())


def day_budget():  # returns the budget for the day
    return allowance[day_name]


def week_budget():  # returns the budget for the week
    global w_budget
    w_budget = sum(budget)
    return w_budget


def month_budget(days):  # returns the budget for the month
    global m_budget
    m_budget = 0
    for day in days:
        m_budget += allowance[day]
    return m_budget


def year_budget():  # returns the budget for the year
    return monthly_allowance * 12


# calculations for no. of days using datetime module
now = datetime.now()
day_name = now.strftime('%A')
days_in_month = calendar.monthrange(now.year, now.month)[1]
first_day = datetime(now.year, now.month, 1)
days_passed = now.day - first_day.day
all_days_until_end_of_month = [first_day + timedelta(days=day) for day in range(days_passed, days_in_month)]

days_left = [day.strftime("%A") for day in all_days_until_end_of_month]
m_budget = month_budget(days_left)


# print("All days until the end of the month:", days_left)
class Colors:  # colourization of the output
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'


if day_name == 'Sunday':
    c = Colors.GREEN
elif day_name == 'Saturday':
    c = Colors.YELLOW
else:
    c = Colors.MAGENTA

if m_budget >= monthly_allowance:
    mc = Colors.GREEN
elif m_budget >= 800:
    mc = Colors.BLUE
else:
    mc = Colors.RED

# output
print('\n\tDay:', c + f'{day_name}' + Colors.RESET)
print("\tToday\'s budget is", c + f"{day_budget()}" + Colors.RESET)
print("\tRemaining allowance for the month:", mc + f"{monthly_allowance - m_budget}\n" + Colors.RESET)
print("\tThis month\'s remaining budget:", mc + f"{m_budget}" + Colors.RESET)

while True:  # loop for user input
    user = input('\n\n Press y for the yearly budget and w for this week\'s budget\n Type edit to re-enter budget'
                 '\n and any other to exit: ')
    user = user.lower()
    if user != 'w' and user != 'y' and user != 'edit':
        break
    elif user == 'y':
        print(f'\n\tYearly budget is: {year_budget()}')
    elif user == 'w':
        print(f"\n\tThis week\'s budget is: {week_budget()}")
    elif user == 'edit':
        import tkinter as tk
        from tkinter import messagebox

        def calculate_allowance():
            global allowance, monthly_allowance

            try:
                entries = []
                for day_entry in day_entries:
                    value = day_entry.get().strip()
                    if value:
                        entries.append(float(value))
                    else:
                        entries.append(0)

                if not any(entries) and not monthly_entry.get().strip():
                    messagebox.showerror("Error",
                                         "Please provide either the allowance for weekdays or the monthly allowance.")
                    return

                weekdays_allowance = sum(entries)
                monthly_allowance = float(
                    monthly_entry.get()) if monthly_entry.get().strip() else weekdays_allowance * 4

                # Update the allowance dictionary
                allowance = {'Monday': entries[0], 'Tuesday': entries[1], 'Wednesday': entries[2],
                             'Thursday': entries[3], 'Friday': entries[4], 'Saturday': entries[5], 'Sunday': entries[6]}

                weekdays_label.config(text=f"Weekdays Allowance: Rs {weekdays_allowance:.2f}", bg="#233D4D",
                                      fg="#FFFFFF")
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

        tk.Label(root, text="Monthly Allowance:", bg="#D3D0CB", fg="#233D4D").grid(row=7, column=0, padx=5, pady=5,
                                                                                   sticky="w")
        tk.Label(root, text="Rs:", bg="#D3D0CB", fg="#233D4D").grid(row=7, column=1, padx=5, pady=5)
        monthly_entry = tk.Entry(root, bg="#FFFFFF")
        monthly_entry.grid(row=7, column=2, padx=5, pady=5, sticky="we")

        weekdays_label = tk.Label(root, text="Weekdays Allowance: Rs 0.00", bg="#233D4D", fg="#FFFFFF")
        weekdays_label.grid(row=8, column=0, columnspan=3, pady=5, sticky="we")

        monthly_label = tk.Label(root, text="Monthly Allowance: Rs 0.00", bg="#233D4D", fg="#FFFFFF")
        monthly_label.grid(row=9, column=0, columnspan=3, pady=5, sticky="we")

        calculate_button = tk.Button(root, text="Feed", command=lambda: calculate_allowance(), bg="#233D4D",
                                     fg="#FFFFFF")
        calculate_button.grid(row=10, columnspan=3, pady=10, sticky="we")

        for i in range(11):
            root.grid_rowconfigure(i, weight=1)

        for j in range(3):
            root.grid_columnconfigure(j, weight=1)

        root.mainloop()
        print("Updated allowance:", allowance)
        print("Updated monthly allowance:", monthly_allowance)
        break


