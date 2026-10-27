patients = [
    ("Ravi", 500, 1200, 3500, "Y", "N", 4500),
    ("Meena", 400, 800, 1800, "N", "Y", 2500),
    ("Kiran", 300, 500, 1000, "N", "N", 1800)
]
for patient in patients:
    name, consultation, diagnostics, treatment, senior, low_income, paid = patient
    if consultation < 0 or diagnostics < 0 or treatment < 0 or paid < 0:
        print(name, "- Invalid billing data")
    else:
        subtotal = consultation + diagnostics + treatment
        concession = 0
        if senior == "Y":
            concession = subtotal * 0.10
        after_senior = subtotal - concession
        if low_income == "Y":
            extra_concession = after_senior * 0.05
        else:
            extra_concession = 0
        final_bill = after_senior - extra_concession
        balance = final_bill - paid
        if balance <= 0:
            status = "Paid"
            balance = 0
        else:
            status = "Balance Due"
        print(
            "Patient:", name,
            "| Subtotal:", round(subtotal, 2),
            "| Concession:", round(concession + extra_concession, 2),
            "| Final bill:", round(final_bill, 2),
            "| Paid:", paid,
            "| Balance:", round(balance, 2),
            "| Status:", status
        )
