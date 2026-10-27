products = [
    ("Notebook", 100, 10, 0.05),
    ("Pen Pack", 50, 10, 0.05),
    ("School Bag", 1200, 1, 0.12)
]

subtotal = 0

# Calculate subtotal
for product in products:
    name, price, quantity, tax_rate = product
    subtotal += price * quantity

# Check discount eligibility
if subtotal >= 2000:
    discount = min(subtotal * 0.10, 300)
else:
    discount = 0

# Calculate tax after discount
tax_total = 0

for product in products:
    name, price, quantity, tax_rate = product

    line_total = price * quantity
    line_discount = discount * line_total / subtotal
    discounted_line = line_total - line_discount

    tax_total += discounted_line * tax_rate

# Calculate final bill
final_total = subtotal - discount + tax_total

# Display invoice
print("RETAIL INVOICE")
print("------------------------------")

for product in products:
    name, price, quantity, tax_rate = product
    print(name, "x", quantity, "=", round(price * quantity, 2))

print("------------------------------")
print("Subtotal: Rs.", round(subtotal, 2))
print("Discount: Rs.", round(discount, 2))
print("Tax: Rs.", round(tax_total, 2))
print("Final total: Rs.", round(final_total, 2))