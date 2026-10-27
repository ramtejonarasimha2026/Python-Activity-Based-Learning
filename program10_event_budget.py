venue_cost = 8000
equipment_cost = 4000
catering_per_person = 150
transport_per_person = 50
certificate_per_person = 20
sponsorship = 5000
expected_participants = 100
registration_fee = 300

# Calculate fixed and variable costs
fixed_cost = venue_cost + equipment_cost
variable_cost = catering_per_person + transport_per_person + certificate_per_person

# Calculate total event cost
total_cost = fixed_cost + variable_cost * expected_participants

# Calculate amount to be covered after sponsorship
amount_to_cover = total_cost - sponsorship
required_fee = amount_to_cover / expected_participants

# Calculate contribution per registration
contribution_per_registration = registration_fee - variable_cost

# Display financial summary
print("Total event cost: Rs.", total_cost)
print("Sponsorship: Rs.", sponsorship)
print("Amount to be covered: Rs.", amount_to_cover)
print("Required fee per participant: Rs.", round(required_fee, 2))

# Calculate break-even registrations
if contribution_per_registration <= 0:
    print("Break-even is not possible at this registration fee.")
else:
    amount_after_sponsorship = fixed_cost - sponsorship

    if amount_after_sponsorship <= 0:
        minimum_registrations = 0
    else:
        minimum_registrations = (
            amount_after_sponsorship + contribution_per_registration - 1
        ) // contribution_per_registration

    print("Minimum registrations to break even:", minimum_registrations)