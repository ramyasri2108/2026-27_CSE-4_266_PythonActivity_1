
n = int(input("Enter number of passengers: "))

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance (km): "))

    print("Classes: Sleeper, AC3, AC2, AC1")
    travel_class = input("Enter travel class: ").upper()

    status = input("Enter ticket status (Booked/Cancelled): ").lower()

    if age < 0 or distance <= 0:
        print("Invalid age or distance!")
        continue

    if travel_class not in ["SLEEPER", "AC3", "AC2", "AC1"]:
        print("Invalid travel class!")
        continue

    if status not in ["booked", "cancelled"]:
        print("Invalid ticket status!")
        continue

    if distance <= 100:
        base_fare = distance * 2
    elif distance <= 500:
        base_fare = 100 * 2 + (distance - 100) * 1.5
    else:
        base_fare = 100 * 2 + 400 * 1.5 + (distance - 500) * 1

    multiplier = {
        "SLEEPER": 1,
        "AC3": 2,
        "AC2": 3,
        "AC1": 4
    }

    fare = base_fare * multiplier[travel_class]

    if age < 5:
        concession = fare
    elif age >= 60:
        concession = fare * 0.20
    else:
        concession = 0

    discounted_fare = fare - concession

    reservation_fee = 40

    total = discounted_fare + reservation_fee

   
    if status == "cancelled":
        penalty = discounted_fare * 0.25
        refund = total - penalty

        print("\n--- CANCELLATION DETAILS ---")
        print("Passenger:", name)
        print("Basic Fare:", round(fare, 2))
        print("Concession:", round(concession, 2))
        print("Reservation Fee:", reservation_fee)
        print("Cancellation Penalty:", round(penalty, 2))
        print("Refund Amount:", round(refund, 2))

    else:
        print("\n--- RAILWAY TICKET DETAILS ---")
        print("Passenger:", name)
        print("Travel Class:", travel_class)
        print("Distance:", distance, "km")
        print("Basic Fare:", round(fare, 2))
        print("Age Concession:", round(concession, 2))
        print("Reservation Fee:", reservation_fee)
        print("Final Payable:", round(total, 2))

print("\nRailway Fare Calculation Completed.")

