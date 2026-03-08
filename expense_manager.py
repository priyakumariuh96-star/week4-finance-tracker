from finance_tracker.expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_all_expenses(self):
        return self.expenses

    def search_by_category(self, category):
        return [e for e in self.expenses if e.category.lower() == category.lower()]
