def calculate_water_bill(units):

    if units <= 10:
        charge = units * 5

    elif units <= 20:
        charge = (10 * 5) + (units - 10) * 8

    elif units <= 30:
        charge = (10 * 5) + (10 * 8) + (units - 20) * 12

    else:
        charge = (10 * 5) + (10 * 8) + (10 * 12) \
                 + (units - 30) * 15

    fixed_fee = 50

    penalty = 100 if units > 30 else 0

    total_bill = charge + fixed_fee + penalty

    return charge, fixed_fee, penalty, total_bill

households = []

n = int(input("Enter number of households: "))

for i in range(n):
    print("\nHousehold", i + 1)

    name = input("Enter household name: ")
    units = float(input("Enter water consumption (KL): "))

    if units < 0:
        print("Invalid consumption. Enter a non-negative value.")
        continue

    charge, fixed, penalty, total = calculate_water_bill(units)

    households.append({
        "name": name,
        "units": units,
        "charge": charge,
        "fixed": fixed,
        "penalty": penalty,
        "total": total
    })

print("\n------ WATER BILL REPORT ------")

total_revenue = 0

for h in households:
    print("\nHousehold:", h["name"])
    print("Consumption:", h["units"], "KL")
    print("Water Charge: Rs.", h["charge"])
    print("Fixed Fee: Rs.", h["fixed"])
    print("Penalty: Rs.", h["penalty"])
    print("Total Bill: Rs.", h["total"])

    total_revenue += h["total"]

if households:
    highest = max(households, key=lambda x: x["units"])

    print("\n------ CONSUMPTION ANALYSIS ------")
    print("Highest Consumer:", highest["name"])
    print("Highest Usage:", highest["units"], "KL")

    print("\nExcessive Usage Households:")

    excessive = [h for h in households if h["units"] > 30]

    if excessive:
        for h in excessive:
            print(h["name"], "-", h["units"], "KL")
    else:
        print("No excessive usage detected.")

    print("\nTotal Revenue: Rs.", total_revenue)
    print("Households Billed:", len(households))

else:
    print("No valid household records available.")

