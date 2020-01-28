#coding challenge
#1.  

#2. 1 mb=8000000 b   1 Gb= 8589934592 b

#3.program for 5 subjects marks

Sub1=int(input("Enter marks for 1: "))
Sub2=int(input("Enter marks for 2: "))
Sub3=int(input("Enter marks for 3: "))
Sub4=int(input("Enter marks for 4: "))
Sub5=int(input("Enter marks for 5: "))

perc=int(Sub1+Sub2+Sub3+Sub4+Sub5)/5

#percentage is perc

if perc>=90:
    print("A")
elif 70<=perc<89:
    print("B")
elif 50<=perc<69:
    print("C")
elif 30<=perc<49:
    print("D")
else:
    print("E")



#4. program for login password

login=input(str("Enter Username: "))
passw=input(str("Enter password: "))
if login == "Priyesh" is True:
    if passw == "password" is True:
        print("Entered the System")
    elif
        print("password do not match")
    else:
        print("Username doesnot Exist")
