from datetime import datetime
from math import ceil

rates = {
    "bike": 10,
    "car": 20,
    "bus": 40
}

daily_limits = {
    "bike": 100,
    "car": 200,
    "bus": 400
}

vehicle_no = input("Enter vehicle number: ")
vehicle_type = input("Enter vehicle type (Bike/Car/Bus): ").lower()

entry = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")

try:

    start = datetime.strptime(entry, "%H:%M")
    end = datetime.strptime(exit_time, "%H:%M")

    if vehicle_type not in rates:
        print("Invalid vehicle category!")

    else:
        duration = (end - start).total_seconds() / 3600

        if duration < 0:
            duration += 24

        if duration == 0:
            print("Invalid parking duration!")

        else:
            hours = ceil(duration)

            rate = rates[vehicle_type]
            daily_limit = daily_limits[vehicle_type]

            days = hours // 24
            remaining_hours = hours % 24

            charge = days * daily_limit
            charge += min(remaining_hours * rate, daily_limit)

            penalty = 100 if duration > 24 else 0

            total = charge + penalty

            print("\n----- PARKING RECEIPT -----")
            print("Vehicle Number:", vehicle_no)
            print("Vehicle Type:", vehicle_type.title())
            print("Parking Duration:", round(duration, 2), "hours")
            print("Hourly Rate: Rs.", rate)
            print("Parking Charge: Rs.", charge)
            print("Penalty: Rs.", penalty)
            print("Total Parking Fee: Rs.", total)

except ValueError:
    print("Invalid time format! Enter time in HH:MM format.")

