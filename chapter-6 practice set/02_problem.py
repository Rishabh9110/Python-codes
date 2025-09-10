name=input("enter the name of student:")
sub1=int(input("enter the maths marks:"))
sub2=int(input("enter the hindi marks:"))
sub3=int(input("enter the physics marks:"))
per1=(sub1/100)*100
per2=(sub2/100)*100
per3=(sub3/100)*100
per=((sub1+sub2+sub3)/300)*100
if(per1>=33 and per2>=33 and per3>=33 and per>40):
    print(f"{name} is passed")
else:
    print(f"{name} is failed")