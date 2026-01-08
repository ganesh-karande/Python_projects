pin = 1234

user = int(input("\nEnter the pin = "))

if pin == user:
    print("\nWlecome to ABC Bank")

    balance = 0
    while True:
        print("""
        1. Deposit 
        2. Withdraw
        3. Balance Check
        4. Exit
        """)

        choice = int(input("Enter your choice : "))

        if choice == 1:
            deposit = int(input("\nEnter the amount to be deposit : "))
            if (deposit>0):
                balance += deposit
                print(f"\n{deposit}rs is successfully deposited")
            else:
                print("\nrequired amount is greater than 0 rs ")
                

        elif choice == 2:
            Withdraw = int(input("\nEnter the Withdraw amount : "))
            if balance>=Withdraw and Withdraw > 0:
                balance -= Withdraw
                print(f"\n{Withdraw} this amount is successfully Withdrawl")
            else:
                print("\nyour available balance is low !!!!!!!!! ")

        elif choice == 3:
            if balance > 0:
                print("\nYour current Balance is : ", balance)
            else:
                print("\ninsufficient balance 😒")

        elif choice == 4:
            break

        else:
            print("\ninvalid choice ❌")

else:
    print("Invalid Pin ❌")
    print()