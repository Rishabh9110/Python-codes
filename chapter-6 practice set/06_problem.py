#write a program to find about wheather the given post is talking about harry or not
para=("""Harry woke up early.
HaRRy packed his bag.
HaRRy started his journey.
HaRRy met his friends.
HaRRy smiled at them.
HaRRy promised to return soon.
HaRRy walked ahead bravely.""")
if("Harry".lower() in para.lower()):
    print("given post is taking about harry")
else:
    print("the given post is not taking about harry")