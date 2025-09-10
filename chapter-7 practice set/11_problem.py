#write a program to rprint multiplication table of n using for loops in reverse
n = int(input("Enter the number: "))
for i in range(1,11):
    print(n*(11-i))