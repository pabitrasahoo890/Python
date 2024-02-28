val = input("Choose one option\n 1.Create Account \n 2. Login \n 3.Exit\n")

if(val=='1'):
    username = input("Enter username: ")
    password = input("Enter Password: ")
    cPassword = input("Re-Enter Password: ")
    balance = input("Enter amount: ")

    if(password == cPassword):
        file = open('accounts.txt', 'a')
        file.write(username + "," + password + "," + balance + "\n")
        print("Account created successfully with amount Rs.", balance)
        file.close()

    else:
        print("Password doesn't match")


elif(val=='2'):
    username = input("Enter username: ")
    password = input("Enter Password: ")

    file = open('accounts.txt', 'r')
    lines = file.readlines()
    # file.close()
    # print(lines)
    found=False
    for line in lines:
        info = line.split(",")
        if(info[0]==username and info[1]==password):
            print("Login Successfull!")
            found=True
            break
    
    if(found==False):
        print("Invalid Credentials.")

    if(found):
        print("1.Check Balance \n 2.Deposit Amount \n 3.Withdraw Amount \n ")
        opt = input("Choose one option from above: ")
        if(opt=='1'):
            file = open('accounts.txt', 'r')
            lines = file.readlines()
            # file.close()
            for line in lines:
                info = line.split(",")
                if(info[0] == username):
                    print("Your current balance is Rs." ,info[2])
                    file.close()
                    break


        elif(opt=='2'):
            depoAmount = input("Enter amount you want to deposit: ")
            file = open('accounts.txt', 'r+')
            lines = file.readlines()
            # file.close()
            for line in lines:
                info = line.split(",")
                if(info[0]==username):
                    bal = float(info[2]) + float(depoAmount)

                    # file.remove()
                    file.write("\n" + username + "," + password + "," + str(bal))
                    print("Your current balance is Rs.",bal)

        elif(opt == '3'):
            withAmount = input("Enter amount you want to withdraw: ")
            file = open('accounts.txt', 'r+')
            lines = file.readlines()
            # file.close()
            for line in lines:
                info = line.split(",")
                if(info[0]==username):
                    bal = float(info[2]) - float(withAmount)

                    # file.remove()
                    file.write("\n" + username + "," + password + "," + str(bal))
                    print("Your current balance is Rs.",bal)

        elif(opt=='3'):
            pass



elif(val=='3'):
    print("Exit Successfull!")



# val = input("Choose any one option \n 1. Create account\n 2. Login\n 3. Exit\n")

# if(val == '1'):
#     username = input("Enter user name: ")
#     password = input("Enter password: ")
#     Cpassword = input("Re-enter password: ")
#     balance = input("Enter deposit amount: ")

#     if(password == Cpassword):
#         file = open("account.txt","a")
#         file.write(username + "," + Cpassword + "," + balance +"\n")
#         print("Account created successfully with deposit amount Rs.", balance)

#     else:
#         print("Password doesn't match")
# elif(val == '2'):
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     file = open("account.txt","r")
#     lines = file.readline()
#     found = False
#     for line in lines:
#         info = line.split(",")
#         if(info[0] == username and info[1] == password):
#             print("Login successful")
#             found = True
#             break
#     if(found == False):
#         print("Invalid credential")

#     if(found):
#         print("1.Check Balance \n 2.Deposit Amount \n 3.Withdraw Amount \n ")
#         opt = input("Choose one option from above")
#         if(opt == '1'):
#             file = open("account.txt","r")
#             lines = file.readline()
#             for line in lines:
#                 info = line.split(",")
#                 if(info[0] == username):
#                     print("Your current balance is Rs.",info[2])
#                     file.close()
#                     break
#         elif(opt == '2'):
#             depoAmount = input("Enter amount want to deposit: ")
#             file = open("account.txt","r")
#             lines = file.readline()
#             for line in lines:
#                 info = line.split(",")
#                 if(info[0] == username):
#                     bal = float(info[2]) + float(depoAmount)
#                     file.write("\n" + username + "," + password + "," + str(bal))
#                     print("Your current balance is Rs. ",bal)

#         elif(opt == '3'):
#             withAmount = input("Enter amount you want to withdraw: ")
#             file = open('account.txt', 'r+')
#             lines = file.readlines()
#             # file.close()
#             for line in lines:
#                 info = line.split(",")
#                 if(info[0]==username):
#                     bal = float(info[2]) - float(withAmount)

#                     # file.remove()
#                     file.write("\n" + username + "," + password + "," + str(bal))
#                     print("Your current balance is Rs.",bal)

# elif(val == '3'):
#     print("Exit Successfull!")


