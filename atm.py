print("-------------------------------------------------------ZETA BANK ATM "
      "MACHINE----------------------------------------------------")


def atm_machine():
    while True:
        greeting = input("\nPlease enter your full_name here: ")
        print(f"\nWelcome {greeting} to ZETA BANK ATM")
        default_pass = 1234
        account_balance = 2000000
        print(f"Your Default Password is {default_pass} ")
        print(f"\nKindly Login with your password {greeting}")
        password = int(input("Input your Password: "))

        if password == default_pass:
            print(f"\nLogin Successful {greeting} you can proceed")

            """
            question = input("Do you wish to continue answer y or n? ")
            if question == "y":
                continue
            else:
                break
            """

            commands = input("Type 0 to continue: ")
            if commands == "0":
                atm_options = """
              Select by typing the Number Id 

              1. Pay Bills                              2. Withdraw

              3. Check Account Status                   4. Check Balance

              5. Make Transfer                          6. Cardless Withdraw

              7. Request Check                          8. Card Policy Restriction    
                   """
                print(atm_options)

                options = input("Please select from the options above by number: ")
                if options == "1":
                    print("""
                    
            You select PayBills Option
            
            1. Electricity Bills        2. Airtime / Data
            
            3. Water Bills              4. DSTV / GOTV Subscriptions
            
            5. STARTIME Subscriptions   6. Others
                    """)
                    new_options = input("Please select from the options above by number: ")
                    if new_options == "1":
                        print("Electricity Bills Selected")
                        elect_bills = input("How much are you paying for electricity: ")
                        bill_no = input("Enter your NEPA Bill Number: ")
                        nepa_account = input("Enter the NEPA account number to transfer to: ")
                        nepa_bank = input("Enter The NEPA bank name: ")
                        print(f"The sum of {elect_bills} of ID {bill_no} has been paid to NEPA {nepa_account} with "
                              f"the name {nepa_bank} successfully {greeting}")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        wish = input("Do you want to perform another transaction? Type 'Y' or 'N': ")
                        if wish.lower() == "y":
                            continue
                        else:
                            break

                    elif new_options == "2":
                        print("\nAirtime / Data Selected")
                        airtime_bills = input("How much are you recharging for AIRTIME: ")
                        phone_no = input("Enter your Phone Number: ")
                        network = input("Enter your network services e.g. MTN, GLO, ETISALAT etc: ")
                        print(f"The sum of {airtime_bills} has been recharge to {phone_no} with the {network}"
                              f" successfully {greeting}")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        wish = input("Do you want to perform another transaction? Type 'Y' or 'N': ")
                        if wish.lower() == "y":
                            continue
                        else:
                            break

                    elif new_options == "3":
                        print("\nWater Bills Selected")
                        water_bills = input("How much are you paying for water bill: ")
                        water_bill_no = input("Enter your Water Bill Number: ")
                        water_bill_account = input("Enter the Water Company account number to transfer to: ")
                        water_bank = input("Enter The WATER Company bank name: ")
                        print(
                            f"The sum of {water_bills} of ID {water_bill_no} has been paid to WATER {water_bill_account} with "
                            f"the name {water_bank} successfully {greeting}")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        wish = input("Do you want to perform another transaction? Type 'Y' or 'N': ")
                        if wish.lower() == "y":
                            continue
                        else:
                            break

                    elif new_options == "4":
                        print("\nDSTV / GOTV Subscriptions Selected")
                        dstv_bills = input("How much are you paying for DSTV / GOTV bill: ")
                        dstv_bill_no = input("Enter your IUC Number: ")
                        dstv_bill_account = input("Enter the DSTV / GOTV account number to transfer to: ")
                        dstv_bank = input("Enter The DSTV / GOTV bank name: ")
                        print(
                            f"The sum of {dstv_bills} of IUC {dstv_bill_no} has been paid to DSTV / GOTV {dstv_bill_account} with "
                            f"the name {dstv_bank} successfully {greeting}")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        wish = input("Do you want to perform another transaction? Type 'Y' or 'N': ")
                        if wish.lower() == "y":
                            continue
                        else:
                            break

                    elif new_options == "5":
                        print("\nSTARTIME Subscriptions Selected")
                        start_bills = input("How much are you paying for STARTIME bill: ")
                        start_bill_no = input("Enter your IUC Number: ")
                        start_bill_account = input("Enter the STARTIME Company account number to transfer to: ")
                        start_bank = input("Enter The STARTIME bank name: ")
                        print(
                            f"The sum of {start_bills} of IUC {start_bill_no} has been paid to STARTIME {start_bill_account} with "
                            f"the name {start_bank} successfully {greeting}")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        wish = input("Do you want to perform another transaction? Type 'Y' or 'N': ")
                        if wish.lower() == "y":
                            continue
                        else:
                            break

                    elif new_options == "6":
                        print("\nOTHERS Selected")
                        other = input("What are other bills are you Transacting? ")
                        other_bills = input("How much are you paying for Other bill: ")
                        other_bill_no = input("Enter your ID Number: ")
                        other_bill_account = input("Enter the Other Company account number to transfer to: ")
                        other_bank = input("Enter The Other bank name: ")
                        print(
                            f"The sum of {other_bills} of ID {other_bill_no} has been paid to OTHER {other_bill_account} with "
                            f"the name {other_bank} of services {other} successfully {greeting}")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        wish = input("Do you want to perform another transaction? Type 'Y' or 'N': ")
                        if wish.lower() == "y":
                            continue
                        else:
                            break

                    else:
                        print(f"Please enter a valid command {greeting}")
                        continue

                elif options == "2":
                    print("""
            You Selected Withdraw Options
                      
            Select an Amount from below options
            
            1. N500                   2. N1000
            
            3. N2000                  4. N3000
            
            5. N5000                  6. N10,000
            
            7. N20,000                8. Others
                      """)

                    withdraw_cmd = input("How much do you want to Withdraw? ")

                    if withdraw_cmd == "1":
                        print("Withdrawing N500 in progress. Please take your cash below")
                        print("DONE.....")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        wish = input("Do you want to perform another transaction? Type 'Y' or 'N': ")
                        if wish.lower() == "y":
                            continue
                        else:
                            print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                            break

                    elif withdraw_cmd == "2":
                        print("Withdrawing N1000 in progress. Please take your cash below")
                        print("DONE.....")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        wish = input("Do you want to perform another transaction? Type 'Y' or 'N': ")
                        if wish.lower() == "y":
                            continue
                        else:
                            break


                    elif withdraw_cmd == "3":
                        print("Withdrawing N2000 in progress. Please take your cash below")
                        print("DONE.....")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        break

                    elif withdraw_cmd == "4":
                        print("Withdrawing N3000 in progress. Please take your cash below")
                        print("DONE.....")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        wish = input("Do you want to perform another transaction? Type 'Y' or 'N': ")
                        if wish.lower() == "y":
                            continue
                        else:
                            break


                    elif withdraw_cmd == "5":
                        print("Withdrawing N5000 in progress. Please take your cash below")
                        print("DONE.....")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        break

                    elif withdraw_cmd == "6":
                        print("Withdrawing N10,000 in progress. Please take your cash below")
                        print("DONE.....")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        break

                    elif withdraw_cmd == "7":
                        print("Withdrawing N20,000 in progress. Please take your cash below")
                        print("DONE.....")
                        print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                        break

                    elif withdraw_cmd == "8":
                        print("\n Maximum amount you can Withdraw is N30,000 on this ATM MACHINE")
                        other_cmd = int(input("Enter your amount here: "))
                        if other_cmd <= 30000:
                            print(f"Withdrawing {other_cmd} in progress. Please take your cash below")
                            print("DONE.....")
                            print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                            break

                        else:
                            print("The amount you entered is greater than what we can dispense. Kindly Retry")
                            continue

                elif options == "3":
                    print("\nCheck Account Status Selected")

                    status = int(input("ENter your account number: "))
                    print(f"Your Account Status {status} is still active and not in domant")
                    print(f"\n Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")
                    wish = input("Do you want to perform another transaction? Type 'Y' or 'N': ")
                    if wish.lower() == "y":
                        continue
                    else:
                        break


                elif options == "4":
                    print("\nCheck Account Balance Option Selected")
                    print(f"Your Account Balance is {account_balance}")
                    print(f"Thank you for Transacting with ZETA BANK. Do have a great day {greeting}")

                    wish = input("Do you want to perform another transaction? Type 'Y' or 'N': ")
                    if wish.lower() == "y":
                        continue
                    else:
                        break


                else:
                    print("Invalid options selected try again")
                    continue

            else:
                print("Please Enter a Valid Commands to continue")

        else:
            print(f"You entered an Incorrect Password please try again later {greeting}")
            break


atm_machine()
