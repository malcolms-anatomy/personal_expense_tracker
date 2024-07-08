# src/gui.py

import tkinter as tk
from tkinter import messagebox
from expense_tracker import ExpenseTracker
from utils import validate_date

class ExpenseTrackerApp:
    def __init__(self, root):
        self.tracker = ExpenseTracker()
        self.root = root
        self.root.title("Personal Expense Tracker")

        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD)")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.category_label = tk.Label(root, text="Category")
        self.category_label.pack()
        self.category_entry = tk.Entry(root)
        self.category_entry.pack()

        self.amount_label = tk.Label(root, text="Amount")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.description_label = tk.Label(root, text="Description")
        self.description_label.pack()
        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Expenses", command=self.view_expenses)
        self.view_button.pack()

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        description = self.description_entry.get()

        if not validate_date(date):
            messagebox.showerror("Error", "Invalid date format")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return

        self.tracker.add_expense(date, category, amount, description)
        messagebox.showinfo("Success", "Expense added successfully")

    def view_expenses(self):
        expenses = self.tracker.view_expenses()
        view_window = tk.Toplevel(self.root)
        view_window.title("View Expenses")
        text = tk.Text(view_window)
        for expense in expenses:
            text.insert(tk.END, f"{expense['date']} - {expense['category']} - ${expense['amount']} - {expense['description']}\n")
        text.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

