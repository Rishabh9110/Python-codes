#write a program to find the greatest of 4 numers enter by the user
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
num4=int(input("enter the number:"))
if(num1>num2 and num1>num3 and num1>num4):
    print("the greatest number among them is:",num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print("the greatest number among them is:",num2)
elif(num3>num1 and num3>num2 and num3>num4):
    print("the greatest number among them is:",num3)

else:
    print("the greatest among the number is:",num4)