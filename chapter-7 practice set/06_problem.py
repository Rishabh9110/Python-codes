#write a program to calculate factorial of a given number
num=int(input("enter the number:"))
fact=1
i=1
while(i<=num):
    fact=fact*i
    i=i+1
print("The factorial of a given number is:",fact)    