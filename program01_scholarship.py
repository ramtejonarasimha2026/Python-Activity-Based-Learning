
minimum_subject_mark = 50

minimum_aggregate = 70

minimum_attendance = 75

maximum_income = 250000

applicants = [
    ("Anil", 85, 78, 90, 92, 180000),
    ("Bhavya", 75, 72, 80, 80, 220000),
    ("Charan", 75, 72, 80, 88, 200000),
    ("Divya", 65, 70, 72, 90, 150000),
    ("Esha", 90, 88, 92, 70, 120000)
]

eligible = []

rejected = []

for applicant in applicants:
    name, maths, physics, computer, attendance, income = applicant

    aggregate = (maths + physics + computer) / 3

    reason = ""

    if (maths < minimum_subject_mark or
        physics < minimum_subject_mark or
        computer < minimum_subject_mark):
        reason = "Subject mark below minimum"

    elif aggregate < minimum_aggregate:
        reason = "Aggregate below 70%"

    elif attendance < minimum_attendance:
        reason = "Attendance below 75%"

    elif income > maximum_income:
        reason = "Income above limit"

    if reason == "":
        eligible.append(
            (name, maths, physics, computer, attendance, income, aggregate)
        )

    else:
        rejected.append((name, round(aggregate, 2), reason))

for i in range(len(eligible)):
    for j in range(i + 1, len(eligible)):
        first = eligible[i]

        second = eligible[j]

        swap = False

        if first[6] < second[6]:
            swap = True

        elif first[6] == second[6] and first[1] < second[1]:
            swap = True

        elif (first[6] == second[6] and
              first[1] == second[1] and
              first[0] > second[0]):
            swap = True

        if swap:
            eligible[i], eligible[j] = eligible[j], eligible[i]

print("UNIVERSITY SCHOLARSHIP ALLOCATION")

print("--------------------------------")

rank = 1

for student in eligible:
    name, maths, physics, computer, attendance, income, aggregate = student

    print(
        "Rank:", rank,
        "| Name:", name,
        "| Aggregate:", round(aggregate, 2), "%"
    )

    rank += 1

print("\nINELIGIBLE APPLICANTS")

for student in rejected:
    name, aggregate, reason = student

    print(name, "| Aggregate:", aggregate, "% | Reason:", reason)
