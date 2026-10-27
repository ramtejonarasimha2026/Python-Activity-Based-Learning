passengers = [
    ("Anil", 25, 100, "Sleeper"),
    ("Meena", 65, 150, "AC"),
    ("Ravi", 40, 80, "First")
]

rates = {"Sleeper": 1.5, "AC": 3.0, "First": 4.5}
reservation_fee = 40

for passenger in passengers:
    name, age, distance, travel_class = passenger

    base_fare = distance * rates[travel_class]

    if age >= 60:
        concession = base_fare * 0.20
    else:
        concession = 0

    fare_after_concession = base_fare - concession
    total_fare = fare_after_concession + reservation_fee
    cancellation_penalty = fare_after_concession * 0.25

    print("Passenger:", name)
    print("Class:", travel_class)
    print("Total fare: Rs.", round(total_fare, 2))
    print("Cancellation penalty: Rs.", round(cancellation_penalty, 2))
    print("----------------------")