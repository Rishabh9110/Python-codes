#write a program to find wheather a given username contains less than 10 characters or not
name=input("enter your name")
if(len(name)<10):
    print("the username contains less than 10 characters")
else:
    print("the username contain more than or equal to 10 characters")