friends=["apple","orange",5,345.06,False,"akash","rohan"]
print(friends[0])
friends[0]="grapes"
print(friends)
#list are mutables it means we can overwrite the value of the list
#we can store any data type in list
friends.append("rishabh")#appending new data in list
print(friends)
friends=friends[1:4]#list slicing
print(friends)