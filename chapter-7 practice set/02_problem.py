#write a program to greet all the person name stored in list l and which start with s
l=["harry","Sohan","Sachin","rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"welcome {name}")