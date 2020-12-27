"""
ROT13 implementation code written by Susmit Singh (20BBS0018), for round 1 of IEEE selections!
code in python (Python 3.9.1)
"""

s = input("Enter your string: ") #code to be encrypted
encrypt = "" 
for letter in s: #loop to go to every element
    if letter.isupper(): #upper alpha char encryption
        index = ord(letter) - 65
        index = (index + 13)%26
        encrypt += chr(index + 65)
    elif letter.islower(): #lower alpha char encryption
        index = ord(letter) - 97
        index = (index + 13)%26
        encrypt += chr(index + 97)
    else: #if not alpha
        encrypt += letter
print("The encrypted/decrypted string is: " + encrypt) #prints encrypted/decrypted key to STDOUT