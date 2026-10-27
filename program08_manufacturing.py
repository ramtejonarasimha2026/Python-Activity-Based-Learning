quantity = 100
material_rate = 80
labour_rate = 25
machine_cost = 500
wastage_rate = 0.05
selling_price = 150
target_profit = 3000

# Calculate production costs
material_cost = quantity * material_rate
labour_cost = quantity * labour_rate
wastage_cost = material_cost * wastage_rate

total_cost = material_cost + labour_cost + machine_cost + wastage_cost

# Calculate revenue and profit
revenue = quantity * selling_price
profit = revenue - total_cost

# Calculate cost per unit
cost_per_unit = total_cost / quantity

# Display results
print("Material cost: Rs.", material_cost)
print("Labour cost: Rs.", labour_cost)
print("Wastage cost: Rs.", round(wastage_cost, 2))
print("Machine cost: Rs.", machine_cost)
print("Total production cost: Rs.", round(total_cost, 2))
print("Cost per unit: Rs.", round(cost_per_unit, 2))
print("Revenue: Rs.", revenue)
print("Profit: Rs.", round(profit, 2))

# Check profit target
if profit >= target_profit:
    print("Profit target achieved")
else:
    print("Profit target not achieved")