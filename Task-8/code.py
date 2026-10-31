fine_rules = {
    "overspeeding": 1000,
    "signal jumping": 500,
    "no helmet/seatbelt": 500,
    "drunk driving": 10000
}

vehicle_categories = ["two-wheeler", "car", "heavy vehicle"]

violations = []

n = int(input("Enter number of violations: "))

for i in range(n):
    print("\nViolation", i + 1)

    vehicle_no = input("Enter vehicle number: ").strip()
    category = input(
        "Enter vehicle category (Two-wheeler/Car/Heavy Vehicle): "
    ).lower().strip()

    offence = input(
        "Enter offence type: "
    ).lower().strip()

    repeat = input(
        "Is this a repeat offence? (yes/no): "
    ).lower().strip()

    if category not in vehicle_categories:
        print("Invalid vehicle category. Record skipped.")
        continue

    if offence not in fine_rules:
        print("Invalid offence type. Record skipped.")
        continue

    if repeat not in ["yes", "no"]:
        print("Invalid repeat status. Record skipped.")
        continue

    base_fine = fine_rules[offence]

    additional_fine = 0

    if repeat == "yes":
        additional_fine = base_fine * 0.50

    total_fine = base_fine + additional_fine

    disqualification = "No"

    if offence == "drunk driving":
        disqualification = "Review required"

    violations.append({
        "vehicle": vehicle_no,
        "category": category,
        "offence": offence,
        "repeat": repeat,
        "fine": total_fine,
        "disqualification": disqualification
    })

print("\n------ TRAFFIC VIOLATION REPORT ------")

total_collection = 0

for v in violations:
    print("\nVehicle Number:", v["vehicle"])
    print("Category:", v["category"])
    print("Offence:", v["offence"])
    print("Repeat Offence:", v["repeat"])
    print("Final Fine: Rs.", v["fine"])
    print("Disqualification:", v["disqualification"])

    total_collection += v["fine"]

print("\n------ SUMMARY ------")
print("Total Violations:", len(violations))
print("Total Penalty: Rs.", total_collection)

print("\nVehicles Requiring Disqualification Review:")

found = False

for v in violations:
    if v["disqualification"] == "Review required":
        print(v["vehicle"], "-", v["offence"])
        found = True

if not found:
    print("None")
