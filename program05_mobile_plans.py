plans = [
    ("Basic", 199, 2, 300, 28, 50, 0.50),
    ("Smart", 299, 5, 600, 28, 30, 0.40),
    ("Max", 399, 10, 1000, 56, 20, 0.30)
]

required_data = 4
required_calls = 500
required_validity = 28
budget = 350

best_plan = None
best_cost = 0

for plan in plans:
    name, fee, data_limit, call_limit, validity, data_rate, call_rate = plan

    extra_data = max(0, required_data - data_limit)
    extra_calls = max(0, required_calls - call_limit)

    total_cost = fee + extra_data * data_rate + extra_calls * call_rate

    if validity >= required_validity and total_cost <= budget:
        if best_plan is None or total_cost < best_cost:
            best_plan = name
            best_cost = total_cost

if best_plan is not None:
    print("Most economical eligible plan:", best_plan)
    print("Total cost: Rs.", round(best_cost, 2))
else:
    print("No plan meets the given requirements.")