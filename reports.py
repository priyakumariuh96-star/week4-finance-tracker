from collections import defaultdict

def monthly_report(expenses, month):
    return sum(e.amount for e in expenses if e.date.startswith(month))

def category_breakdown(expenses):
    result = defaultdict(float)
    for e in expenses:
        result[e.category] += e.amount
    return result
