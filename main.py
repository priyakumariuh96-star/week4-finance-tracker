from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import load_expenses, save_expenses
from finance_tracker.reports import monthly_report, category_breakdown
from finance_tracker.utils import print_line

class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        self.manager.expenses = load_expenses()

    def run(self):
        print_line()
        print("          PERSONAL FINANCE TRACKER")
        print_line()

        while True:
            print("\n" + "=" * 40)
            print("              MAIN MENU")
            print("=" * 40)
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. Search Expenses")
            print("4. Generate Monthly Report")
            print("5. View Category Breakdown")
            print("0. Exit")
            print("=" * 40)

            choice = input("Enter your choice (0-5): ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.search_expenses()
            elif choice == "4":
                self.monthly()
            elif choice == "5":
                self.category()
            elif choice == "0":
                print_line()
                print("Thank you for using Personal Finance Tracker!")
                print_line()
                break
            else:
                print("Invalid choice!")

    def add_expense(self):
        print("\n--- ADD NEW EXPENSE ---")
        date = input("Date (YYYY-MM-DD): ")
        amount = float(input("Amount: "))
        category = input("Category: ")
        desc = input("Description: ")

        self.manager.add_expense(Expense(date, amount, category, desc))
        save_expenses(self.manager.expenses)
        print("Expense added successfully!")

    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        for e in self.manager.get_all_expenses():
            print(e.date, e.amount, e.category, e.description)

    def search_expenses(self):
        cat = input("Enter category: ")
        results = self.manager.search_by_category(cat)
        for e in results:
            print(e.date, e.amount, e.description)

    def monthly(self):
        month = input("Enter month (YYYY-MM): ")
        print("Total:", monthly_report(self.manager.expenses, month))

    def category(self):
        data = category_breakdown(self.manager.expenses)
        for k, v in data.items():
            print(k, ":", v)
