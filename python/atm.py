# ATM simulation
print("Welcome to the Broke ATM \n An ATM for the brokes like you")

print("Did you inserted your card you broke?")
inserted = input("yes or no: ")
inserted.lower()
if(inserted == "yes"):
    acb = 100000
    passwdd=1234
    print("Ahh i see good then \n Now chopose what language you bark")
    lang = int(input("1.Kannada \n 2.English\n3.Cant speeak too dumb : "))
    acc = int(input("Choose account type \n1.Savings \n2.Current : "))
    if(acc==1):
        print("Welcome brokie didnt knew you saved some changes")
        choice=int(input("Now choose what you wanna do \n 1.Withdraw \n2.Deposit\n3.check balance : "))
        if(choice == 1):
            wamt = int(input("Enter amount you beggar : "))
            if(wamt > acb):
                print("hah beggar you dont have that much and nor are you allowed to have that much")
            else:
                passwd = int(input("Enter the password beggar : "))
                if(passwd == passwdd):
                    acb -= wamt
                    print("here take this")
                    print("wait for the slip beggar")
                    print(f"--------BROKE ATM----------\n transcation id WhoCaresDumb23 \n Withdrawl amount {wamt}\n balance {acb}\n----------End--------------")
                else:
                    print("FOrgot your password you idiot")
        elif(choice==2):
            print("phew didnt knew we had an big shot here\n you have money to deposit?")
            damt=int(input("Enter amount big guy : "))
            passwd = int(input("Enter the password beggar : "))
            if(passwd == passwdd):
                acb += damt
                print("here take this")
                print("wait for the slip big guy")
                print(
                    f"--------BROKE ATM----------\n transcation id ICareDumb23 \n Withdrawl amount {damt}\n balance {acb}\n----------End--------------"
                )
            else:
                print("FOrgot your password you idiot")
        elif(choice==3):
            passwd = int(input("Enter the password beggar : "))
            if passwd == passwdd:
                print(f"here you have {acb} chillars")
        else:
            print("No one taught you to read you dumb")
else :
    print("Welcome brokie didnt knew you were  some big shot")
    choice = int(
            input(
                "Now choose what you wanna do \n 1.Withdraw \n2.Deposit\n3.check balance : "
            )
        )
    if choice == 1:
        wamt = int(input("Enter amount you beggar : "))
        if wamt > acb:
            print(
                    "hah beggar you dont have that much and nor are you allowed to have that much"
                )
        else:
            passwd = int(input("Enter the password beggar : "))
            if passwd == passwdd:
                acb -= wamt
                print("here take this")
                print("wait for the slip beggar")
                print(
                    f"--------BROKE ATM----------\n transcation id WhoCaresDumb23 \n Withdrawl amount {wamt}\n balance {acb}\n----------End---------------"
                )
            else:
                print("FOrgot your password you idiot")
    elif choice == 2:
        print(
                "phew didnt knew we had an big shot here\n you have money to deposit?"
            )
        damt = int(input("Enter amount big guy : "))
        passwd = int(input("Enter the password beggar : "))
        if passwd == passwdd:
            acb += damt
            print("here take this")
            print("wait for the slip big guy")
            print(
                f"--------BROKE ATM----------\n transcation id ICareDumb23 \n Withdrawl amount {damt}\n balance {acb}\n----------End--------------"
            )
        else:
            print("FOrgot your password you idiot")
    elif choice == 3:
        passwd = int(input("Enter the password beggar : "))
        if passwd == passwdd:
            print(f"here you have {acb} chillars")
    else:
        print("No one taught you to read you dumb")
