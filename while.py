# Simple ATM Machine
balance = 1000  # Initial balance
pin = "1234"    # Fixed PIN for demo
print("Welcome to the ATM Macchine!")

# Pin check 
enter_pin = input("Enter your 4-digit PIN: ")
while enter_pin != pin:
    print("Incorrect PIN. Try again.")
    enter_pin = input("Enter your 4-digit PIN: ")

# Choose Option 
while True:
    print("\n--- ATM Machine Option ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Your current balance is ₹%s" % (balance))
    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print("₹%s deposited successfully. New balance is ₹%s" % (amount, balance))
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= balance:
            balance -= amount
            print("₹%s withdrawn successfully. Remaining balance is ₹%s" % (amount, balance))
        else:
            print("Insufficient funds!")
    elif choice == "4":
        print("Thank you for ATM Machine. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
