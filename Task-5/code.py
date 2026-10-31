
balance = float(input("Enter initial balance: Rs. "))
limit = float(input("Enter maximum withdrawal limit: Rs. "))
n = int(input("Enter number of transactions: "))

total_deposits = 0
total_withdrawals = 0
successful = 0
rejected = 0

if balance < 0 or limit <= 0 or n < 0:
    print("Invalid account details!")

else:
    for i in range(n):
        print("\nTransaction", i + 1)

        transaction = input("Enter type (Deposit/Withdraw): ").lower()
        amount = float(input("Enter amount: Rs. "))

        if amount <= 0:
            print("Rejected: Invalid amount")
            rejected += 1

        elif transaction == "deposit":
            balance += amount
            total_deposits += amount
            successful += 1
            print("Deposit successful")

        elif transaction == "withdraw":
            if amount > limit:
                print("Rejected: Withdrawal limit exceeded")
                rejected += 1

            elif amount > balance:
                print("Rejected: Insufficient balance")
                rejected += 1

            else:
                balance -= amount
                total_withdrawals += amount
                successful += 1
                print("Withdrawal successful")

        else:
            print("Rejected: Invalid transaction type")
            rejected += 1

        print("Current Balance: Rs.", round(balance, 2))

    print("\n----- ATM TRANSACTION SUMMARY -----")
    print("Total Deposits: Rs.", round(total_deposits, 2))
    print("Total Withdrawals: Rs.", round(total_withdrawals, 2))
    print("Successful Transactions:", successful)
    print("Rejected Transactions:", rejected)
    print("Closing Balance: Rs.", round(balance, 2))

