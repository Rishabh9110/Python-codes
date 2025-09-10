#methods in set
s=set()
#method-1(add-helps in adding elements in the set)
s.add(55)
s.add(77)
print(s)
#method-2(remove-to remove the element from the set)
s.remove(55)
print(s)
#method-3(union-returns a new set fromall the items from both set)
e={1,2,3,4}
f={4,5,6,7}
print(e.union(f))
print(e.intersection(f))#returns a new set with common elements