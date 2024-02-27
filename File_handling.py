ch = input("1 Create\n 2 Login")
if(ch == '1'):
    #create account
    user = input("Username")
    password = input("Password")
    Cpassword = input("Confirm password")
    if(password == Cpassword):
        string=""
        file = open('cre.txt', 'a')
        string+=f',{user}'
        string+=f',{Cpassword}'

        file.write(string)
        file.close()

elif(ch == '2'):
    #reading file
    file = open('cre.txt','r')
    temp = ''
    for x in file.read():
        temp+=x
    temp = temp.split(',')
    mydict = {}
    for x in range(0,len(temp),2):
        mydict[temp[x]]=temp[x+1]
    
    user = input("Enter user name: ")
    Cpassword = input("Enter password: ")
    count=0
    for x in mydict.items():
        if(user == x[0] and Cpassword == x[1]):
            count+=1
    if(count == 1):
        print("Login Success")
    else:
        print("Failed")

