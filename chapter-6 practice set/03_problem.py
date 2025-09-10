#spam detection program
spam1="make a lot of money"
spam2="buy now"
spam3="subscribe this"
spam4="click this"
mess=input("enter the message:")
if(spam1 in mess or spam2 in mess or spam3 in mess or spam4 in mess):
    print(f"spam detected:{spam1}")
else:
    print("mess is not a spam")