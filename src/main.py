# src/main.py

import argparse
from expense_tracker import ExpenseTracker
from gui import ExpenseTrackerApp
import tkinter as tk

def main():
    parser = argparse.ArgumentParser(description='Personal Expense Tracker')
    parser.add_argument('--add', nargs=4, metavar=('DATE', 'CATEGORY', 'AMOUNT', 'DESCRIPTION'), help='Add a new expense')
    parser.add_argument('--view', action='store_true', help='View all expenses')
    parser.add_argument('--categorize', action='store_true', help='View expenses categorized')
    parser.add_argument('--gui', action='store_true', help='Launch the GUI')

    args = parser.parse_args()

    tracker = ExpenseTracker()

    if args.add:
        date, category, amount, description = args.add
        tracker.add_expense(date, category, float(amount), description)
        print(f"Added expense: {date} - {category} - ${amount} - {description}")

    if args.view:
        expenses = tracker.view_expenses()
        for expense in expenses:
            print(f"{expense['date']} - {expense['category']} - ${expense['amount']} - {expense['description']}")

    if args.categorize:
        categorized = tracker.categorize_expenses()
        for category, expenses in categorized.items():
            print(f"Category: {category}")
            for expense in expenses:
                print(f"  {expense['date']} - ${expense['amount']} - {expense['description']}")

    if args.gui:
        root = tk.Tk()
        app = ExpenseTrackerApp(root)
        root.mainloop()

if __name__ == '__main__':
    main()

