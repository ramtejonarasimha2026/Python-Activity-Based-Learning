employees = [
    ("Asha", 22000, 5, 1500),
    ("Balu", 35000, 8, 2500),
    ("Charan", 50000, 10, 4000)
]

for employee in employees:
    name, basic, overtime_hours, incentive = employee

    hra = basic * 0.20
    travel = basic * 0.08
    overtime = overtime_hours * 200

    gross = basic + hra + travel + overtime + incentive

    if gross <= 25000:
        deduction = gross * 0.05
    elif gross <= 50000:
        deduction = 25000 * 0.05 + (gross - 25000) * 0.10
    else:
        deduction = 25000 * 0.05 + 25000 * 0.10 + (gross - 50000) * 0.15

    net = gross - deduction

    print("EMPLOYEE:", name)
    print("Basic:", round(basic, 2), "| HRA:", round(hra, 2), "| Travel:", round(travel, 2))
    print("Overtime:", round(overtime, 2), "| Incentive:", round(incentive, 2))
    print("Gross:", round(gross, 2), "| Deduction:", round(deduction, 2), "| Net:", round(net, 2))
    print("----------------------------------------")