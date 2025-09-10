#write a program to detect double space in string
string=("rishabh is  a bad boy and he dont know how to bheave with anyone")
print(string.find("  "))#it will return the index where double space is
print(string.find("holly"))#if it finds nothing it will return -1
#now we will replace double spacer to single space
print(string)
print(string.replace("  "," "))
#strings are immutable which means that you cannot change them by executing or running function