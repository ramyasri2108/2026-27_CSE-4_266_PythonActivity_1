
patient_name = input("Enter patient name: ")
patient_category = input("Enter patient category (General/Senior): ")

consultation = float(input("Enter consultation charges: ₹"))
diagnostic = float(input("Enter diagnostic charges: ₹"))
treatment = float(input("Enter treatment charges: ₹"))


if min(consultation, diagnostic, treatment) < 0:
    print("Invalid input: Charges cannot be negative.")

elif patient_category.lower() not in ["general", "senior"]:
    print("Invalid patient category.")

else:
    total_bill = consultation + diagnostic + treatment

    concession = 0

    if total_bill >= 5000:
        concession = total_bill * 0.10

    if patient_category.lower() == "senior":
        concession += 0  

    payable = total_bill - concession

    if payable < 2000:
        classification = "Low Payment"
    elif payable < 10000:
        classification = "Medium Payment"
    else:
        classification = "High Payment"

    print("\n--- Hospital Bill ---")
    print("Patient Name:", patient_name)
    print("Patient Category:", patient_category)
    print(f"Total Bill: ₹{total_bill:.2f}")
    print(f"Concession: ₹{concession:.2f}")
    print(f"Final Payable: ₹{payable:.2f}")
    print("Patient Classification:", classification)

