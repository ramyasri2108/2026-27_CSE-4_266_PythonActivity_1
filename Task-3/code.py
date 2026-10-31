
participants = int(input("Enter number of participants: "))

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))
contribution = float(input("Enter contribution per participant: "))

if (participants <= 0 or min(venue, equipment, catering,
        transport, certificate, sponsorship, contribution) < 0):
    print("Invalid input! Enter valid positive values.")

else:
    fixed_cost = venue + equipment

    variable_cost = participants * (
        catering + transport + certificate
    )

    total_expense = fixed_cost + variable_cost

    total_contribution = participants * contribution

    total_funds = total_contribution + sponsorship
    shortfall = max(0, total_expense - total_funds)

    cost_per_person = catering + transport + certificate

    if contribution <= cost_per_person:
        break_even = "Not possible with current contribution"
    else:
        remaining_cost = max(0, fixed_cost - sponsorship)
        break_even = -(-remaining_cost //
                       (contribution - cost_per_person))

    print("\n--- CAMPUS EVENT FINANCIAL REPORT ---")
    print("Total Participants:", participants)
    print("Fixed Cost:", fixed_cost)
    print("Variable Cost:", variable_cost)
    print("Total Event Expense:", total_expense)
    print("Participant Contribution:", total_contribution)
    print("Sponsorship:", sponsorship)
    print("Sponsorship Shortfall:", shortfall)
    print("Break-Even Registrations:", break_even)

