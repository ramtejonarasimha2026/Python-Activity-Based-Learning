expenses = [
    ("Hotel", 100, "USD"),
    ("Food", 3000, "INR"),
    ("Museum", 30, "EUR"),
    ("Transport", 20, "USD")
]

exchange_rates = {"INR": 1, "USD": 83, "EUR": 90}
budget = 15000

total = 0
largest_category = ""
largest_amount = 0

for expense in expenses:
    category, amount, currency = expense

    converted = amount * exchange_rates[currency]

    if currency != "INR":
        converted = converted * 1.02

    print(category, ": Rs.", round(converted, 2))

    total = total + converted

    if converted > largest_amount:
        largest_amount = converted
        largest_category = category

print("--------------------------")
print("Total spending: Rs.", round(total, 2))
print("Largest expense category:", largest_category)

if total <= budget:
    print("Within budget")
else:
    print("Budget exceeded by Rs.", round(total - budget, 2))