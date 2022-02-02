from asyncore import read
import json
from queue import Empty

userList =[]
print("1.Add 2.Update 3.Delete 4.Show Details 5.Exit")
choice = int(input("Enter Your Choice : "))
def starting(choice):
    if choice == 1 :
        print("userInput is Add User...")
        addDetails()
    elif choice == 2 :
        print(f"userInput is {choice}")
    elif choice == 3 :
        print(f"userInput is {choice}")
    elif choice == 4 :
        print(f"userInput is Show Details")
        showDetails()
    elif choice == 5 :
        print(f"userInput is {choice}")
    else :
        print("please enter Valid Input ")

# def userTemplate(userRollNo,userName,userAge,userEMail,userContactNumber,userDOB):
def userTemplate(userRollNo,userName):
    d1 = {
        "RollNo": userRollNo,
        "Name": userName,
        # "Age" : userAge,
        # "Email": userEMail,
        # "Contact Number": userContactNumber,
        # "DOB": userDOB
    }
    userList.append(d1)

def userStoreValues():
    global userList
    f=open("DataBase.json")
    content=f.read()
    f.close()
    if(content == '[]'):
        print("File is Empty")
        with open("DataBase.json","a") as f:
            str1 = json.dump(userList, f, indent=4)
            print(str1)
    else:
        print("File is not empty")
        f=open("DataBase.json")
        # content = f.read()
        # f.close()
        # print(content)
        jsoncontent = json.load(content)
        print(jsoncontent)
        for i in jsoncontent:
            print(i)
        with open("DataBase.json","a") as f:
            str1 = json.dump(userList, f, indent=4)
    
def addDetails():
    userRollNo = input("Enter Your RollNo. : ")
    userName= input("Enter Your Name : ")
    # userAge = int(input("Enter Your Age : "))
    # userEMail = input("Enter Your Email : ")
    # userContactNumber = int(input("Enter Your Number  : "))
    # userDOB = input("Enter Your DOB(DD-MM-YYYY) : ")
    # userTemplate(userRollNo,userName,userAge,userEMail,userContactNumber,userDOB)
    userTemplate(userRollNo,userName)
    more1 =input("Do Your want to enter more User (y/n) : ")
    if(more1=="y" or more1 =="Y"):
        addDetails()
    else:
        userStoreValues()

def showDetails():
    with open("DataBase.json", "r") as read_content:
	    content1 = print(json.load(read_content))
    
starting(choice)