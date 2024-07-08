# tests/test_expense_tracker.py

import unittest
from src.expense_tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_expense(self):
        self.tracker.add_expense('2024-07-08', 'Transport', 20.0, 'Bus fare')
        self.assertEqual(len(self.tracker.view_expenses()), 1)

    def test_categorize_expenses(self):
        self.tracker.add_expense('2024-07-08', 'Food', 15.0, 'Lunch')
        self.tracker.add_expense('2024-07-08', 'Transport', 20.0, 'Bus fare')
        categorized = self.tracker.categorize_expenses()
        self.assertIn('Food', categorized)
        self.assertIn('Transport', categorized)

if __name__ == '__main__':
    unittest.main()

