"""
This program made by Joe
"""
total_balance = 1000
min_bank = 0
loop_overun_protection = 0

while loop_overun_protection < 20:
    user_input = input("deposit or withdrawal? ")
    if user_input == "deposit":
        print("Your current balance is $" + str(total_balance))
        total_balance = total_balance + int(input("How much to deposit? "))
        print("Your current balance is now $" + str(total_balance))
    elif user_input == "withdrawal":
        print("Your current balance is $" + str(total_balance))
        temp_balance = int(input("How much to withdrawal? "))
        if total_balance - temp_balance <= min_bank:
            print("You cannot have a negative balance!")
        else:
            total_balance = total_balance - temp_balance
        print("Your current balance is now $" + str(total_balance))
    else:
        print("Invalid transaction")
    loop_overun_protection = loop_overun_protection + 1