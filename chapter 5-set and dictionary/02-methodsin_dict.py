a={
    "key":"value",
    "name":"harry",
    "rollno":2134,
    "id":4194
}          
#Method-1(items-returns a list of key value tuples)
print(a.items())                                       
#method-2(keys-returns a list containing keys)   
print(a.keys())     
#method-3(update-updates the dictionary with supplied key value pairs)
a.update({"rollno":21})
print(a)
#method-4(get-returnthe value of given key)
print(a.get("name1"))#it will print none
print(a["name1"])#it will provide you an error