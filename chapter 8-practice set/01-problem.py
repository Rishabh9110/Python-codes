# write a program using fuction to fidn greatest of three number
def greatest(a,b,c):

    if(a>b and a>c):
        print(f"{a} is the greatest element")
    if(b>a and b>c):
        print(f"{b} is the greatest element")
    else:
        print(f"{c} is the greatest element")
    return "program completed!"    
            
d=int(input("enter the number 1:"))
e=int(input("enter the number 2:"))
f=int(input("enter the number 3:"))
print(greatest(d,e,f))