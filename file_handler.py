import json
import os
from finance_tracker.expense import Expense

DATA_FILE = "data/expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return [Expense(**item) for item in data]

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=4)
