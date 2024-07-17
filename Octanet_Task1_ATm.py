'''Author- J. Manish                Python Development Internship at Octanet

T A S K - 1
Create an ATM Machine Simulation:
Your program should simulate the basic functions of an ATM machine.

Functions to include:
Account balance inquiry
Cash withdrawal
Cash deposit
PIN change
Transaction history

Program Specifications:
Use Python for your implementation.
Ensure your code is well-documented with comments explaining the functionality of each part.

IDE used: Visual Studio Code
Note: Use VS Code for better experience

ATM PIN: 1432
This ATM Machine Experience has been obtained from the combination of SBI and Union Bank ATM MAchines
'''

# Importing modules
import os
import time


#--------------------------------------FUNCTIONS FOR SAVING TRANSACTION DETAILS------------------------------------------
# Function to generate receipts for the whole transactions
def transactionReceipt(transaction_type, amount):
    timestamp = time.strftime("%d-%m-%Y %H:%M:%S")
    with open("transaction_receipt.txt", "a") as file:
        file.write(f"{timestamp} - {transaction_type}: Rs. {amount}\n")
    print("Transaction receipt generated.")

# Function to generate receipts for the with-draw transactions
def amountWithdrawReceipt(amount, balance):
    timestamp = time.strftime("%d-%m-%Y %H:%M:%S")
    with open("amount_withdraw.txt", "a") as file:
        file.write(f"{timestamp} - SAVINGS BALANCE: Rs. {balance + amount}      WITHDRAW AMOUNT: Rs. {amount}       REMAINING BALANCE: Rs. {balance}\n")
    print("Withdrawal receipt generated.")

# Function to generate receipts for the Deposit transactions
def amountDepositReceipt(amount, balance):
    timestamp = time.strftime("%d-%m-%Y %H:%M:%S")
    with open("amount_deposit.txt", "a") as file:
        file.write(f"{timestamp} - SAVINGS BALANCE: Rs. {balance - amount}      DEPOSIT AMOUNT: Rs. {amount}        NEW BALANCE: Rs. {balance}\n")
    print("Deposit receipt generated.")


#--------------------------------------FUNCTION FOR GIVING REALTIME DEPOSIT / WITHDRAW DETAILS------------------------------------------
# Function to clear receipts for the with-draw and deposited transactions because, it deletes previous transactions
# and only stores present deposit/ withdraw details i.e., gives realtime transaction details.
def clearReceipt(filename):
    with open(filename, "w") as file:
        pass




#The main program and ATM experience starts here
print("\n")
print("                                                        INSERT YOUR ATM CARD") #enter the atm card


print("\n")
print("                              ╔═══════════════════════════════════════════════════════════════════════╗")
print("                              ║               PLEASE WAIT. YOUR TRANSACTION IS PROCESSING             ║")
print("                              ║     YOUR CARD WILL BE RELEASED AFTER THE TRANSACTION IS COMPLETED     ║")
print("                              ╚═══════════════════════════════════════════════════════════════════════╝")
print("\n")

time.sleep(5) #sleeps for 5 seconds

user_atm_pin = 1432 #<== Remember this ATM PIN
incorrect_attempts = 0  #when the user ends 3 incorrect pins, The account will get freezed
user_balance = 77777

while incorrect_attempts <= 2:
    try:
        atm_pin = int(input("ENTER YOUR ATM PIN: ")) #user to enter the PIN
        if atm_pin == user_atm_pin:
            while True:
                print("\n")
                print("         ╭────────────────────────────────────────────────────────────────────────────────────────────────╮")
                print("         │                        PLEASE SELECT THE TRANSACTION BY PRESSING THE KEY                       │")
                print("         │                                                                                                │")
                print("         │                                  1. BALANCE INQUIRY                                            │")
                print("         │                                  2. WITHDRAW                                                   │")
                print("         │                                  3. DEPOSIT                                                    │")
                print("         │                                  4. CHANGE PIN                                                 │")
                print("         │                                  5. TRANSACTION HISTORY                                        │")
                print("         │                                  6. CANCEL                                                     │")
                print("         ╰────────────────────────────────────────────────────────────────────────────────────────────────╯")
                print("\n")

                try:
                    user_choice = int(input("PLEASE SELECT THE TRANSACTION BY PRESSING THE KEY: ")) #User can choose various actions
                    
                    #code for BALANCE INQUIRY
                    if user_choice == 1:
                        print("                              ╔═══════════════════════════════════════════════════════════════════════╗")
                        print(f"                              ║                     YOUR CURRENT BALANCE IS RS. {user_balance}                ║")
                        print("                              ╚═══════════════════════════════════════════════════════════════════════╝")

                    #code for WITHDRAW AMOUNT
                    elif user_choice == 2:
                        user_withdraw_amount = float(input("PLEASE ENTER WHOLE AMOUNT IN RUPEES: "))
                        if user_withdraw_amount <= user_balance: #user can withdraw amount less than or equal to his bank balance only
                            user_balance -= user_withdraw_amount
                            print(f"YOUR CURRENT BALANCE IS RS. {user_balance}")
                            want_receipt = input("DO YOU WANT RECEIPT FOR THIS TRANSACTION? (Y/N): ").lower() #want receipt?
                            if want_receipt == 'y':
                                amountWithdrawReceipt(user_withdraw_amount, user_balance)
                                transactionReceipt("Withdraw", user_withdraw_amount)
                                print("\nYOUR AMOUNT WITHDRAW RECEIPT:")
                                with open("amount_withdraw.txt", "r") as file:
                                    print(file.read())
                                    clearReceipt("amount_withdraw.txt")

                        else:
                            print(f"YOU CANNOT WITHDRAW MONEY EXCEEDING YOUR CURRENT BALANCE!\nYOUR CURRENT BALANCE: {user_balance}")

                    #code for DEPOSIT AMOUNT
                    elif user_choice == 3:
                        user_deposit_amount = float(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT: "))
                        user_balance += user_deposit_amount
                        print(f"YOUR CURRENT BALANCE IS RS. {user_balance}")
                        amountDepositReceipt(user_deposit_amount, user_balance)
                        transactionReceipt("Deposit", user_deposit_amount)

                        print("\nYOUR AMOUNT WITHDRAW RECEIPT:")
                        with open("amount_deposit.txt", "r") as file:
                            print(file.read())
                        clearReceipt("amount_deposit.txt")

                    #code for changing ATM PIN
                    elif user_choice == 4:
                        user_new_atm_pin = int(input("ENTER YOUR NEW ATM PIN: "))
                        verify_atm_pin = int(input("ENTER YOUR PREVIOUS ATM PIN: "))
                        while verify_atm_pin == atm_pin :
                            user_new_atm_pin_confirmation = input("DO YOU WANT TO CONFIRM (Y/N): ").lower()
                            if user_new_atm_pin_confirmation == 'y':
                                user_atm_pin = user_new_atm_pin
                                print("YOUR ATM PIN HAS BEEN SUCCESSFULLY CHANGED")
                                print(f"YOUR ATM PIN IS {user_atm_pin} FROM NOW.")
                                break
                            else:
                                break

                    #code for TRANSACTION HISTORY                    
                    elif user_choice == 5:
                        with open("transaction_receipt.txt", "r") as file:
                            print(file.read())

                    #code for CANCEL and stop the process
                    elif user_choice == 6:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        exit()


                    else:
                        print("INVALID INPUT! SELECT A VALID OPTION!") #user should enter only from 1 to 6 options
                except ValueError:
                    print("INVALID INPUT! PLEASE ENTER A NUMBER.")
                    
        #code for incorrect pin entry   
        else:
            print("INVALID PIN! ENTER THE VALID PIN.")
            incorrect_attempts += 1 #incorrect ATM PIN increases it by +1
    except ValueError:
        print("INVALID INPUT! PLEASE ENTER A NUMBER.")

#3 Incorrect PINS will result in account freeze
else:
    print("\n")
    print("                              ╔════════════════════════════════════════════════════════╗")
    print("                              ║               YOUR ACCOUNT HAS BEEN FROZEN!            ║")
    print("                              ║              CONTACT YOUR BANK IMMEDIATELY!            ║")
    print("                              ╚════════════════════════════════════════════════════════╝")
    print("\n")
