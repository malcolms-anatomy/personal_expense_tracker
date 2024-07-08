# src/expense_tracker.py

import csv
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/expenses.csv')

class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()

    def add_expense(self, date, category, amount, description):
        expense = {
            'date': date,
            'category': category,
            'amount': float(amount),
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        return self.expenses

    def categorize_expenses(self):
        categorized = {}
        for expense in self.expenses:
            category = expense['category']
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(expense)
        return categorized

    def load_expenses(self):
        expenses = []
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row['amount'] = float(row['amount'])
                    expenses.append(row)
        return expenses

    def save_expenses(self):
        with open(DATA_FILE, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
            writer.writeheader()
            writer.writerows(self.expenses)

if __name__ == '__main__':
    tracker = ExpenseTracker()
    tracker.add_expense('2024-07-08', 'Food', 15.00, 'Lunch')
    print(tracker.view_expenses())

