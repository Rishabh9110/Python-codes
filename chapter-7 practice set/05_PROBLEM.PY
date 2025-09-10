#Write a program to find the sum of first n natural number using while loop
num=int(input("enter the number till you want sum:"))
i=0
sum=0
while(i<=num):
    sum=sum+i
    i=i+1
print(f"the sum upto {num} is {sum}")    