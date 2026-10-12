balance = 0.0
transactions = []

while True:
    print("\n Banking Transaction Simulator ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Inquiry")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Error: Amount must be positive.")
            else:
                balance += amount
                transactions.append(("Deposit", amount, balance))
                print(f"Deposit successful. Balance: ₹{balance:.2f}")
        except ValueError:
            print("Error: Please enter a valid number.")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Error: Amount must be positive.")
            elif amount > balance:
                print("Error: Insufficient balance.")
            else:
                balance -= amount
                transactions.append(("Withdrawal", amount, balance))
                print(f"Withdrawal successful. Balance: ₹{balance:.2f}")
        except ValueError:
            print("Error: Please enter a valid number.")

    elif choice == "3":
        print(f"Current balance: ₹{balance:.2f}")

    elif choice == "4":
        if not transactions:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(transaction)

    elif choice == "5":
        print("Thank you for using the Banking Transaction Simulator!")
        break
    else:
        print("Invalid choice. Please select 1-5.")