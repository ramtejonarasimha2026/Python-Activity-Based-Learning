
monthly_units = [80, 120, 190, 280]

fixed_charge = 50

bills = []

for month in range(len(monthly_units)):

    units = monthly_units[month]

    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = 100 * 2 + (units - 100) * 3

    else:
        energy_charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    adjustment = 0

    if units <= 100:
        adjustment = -energy_charge * 0.05

    elif energy_charge > 500:
        adjustment = energy_charge * 0.05

    total_bill = energy_charge + adjustment + fixed_charge

    bills.append(total_bill)

    print(
        "Month", month + 1,
        "| Units:", units,
        "| Energy:", round(energy_charge, 2),
        "| Adjustment:", round(adjustment, 2),
        "| Bill:", round(total_bill, 2)
    )

print("MONTH-TO-MONTH COMPARISON")

for i in range(1, len(bills)):

    increase = bills[i] - bills[i - 1]

    percent = increase / bills[i - 1] * 100

    print("Month", i + 1, "increase:", round(percent, 2), "%")

    if percent > 30:
        print("Unusual increase detected")
