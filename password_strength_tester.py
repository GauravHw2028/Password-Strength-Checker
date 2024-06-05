import string

print("Welcome to Password Strength Checker! \n")
password_input=(input("Enter your password: \n"))

uppercase_test=any([1 if c in string.ascii_uppercase else 0 for c in password_input])
lowercase_test=any([1 if c in string.ascii_lowercase else 0 for c in password_input])
special_test=any([1 if c in string.punctuation else 0 for c in password_input])
digits_test=any([1 if c in string.digits else 0 for c in password_input])
#checks if the password contains at least one uppercase letter, one lowercase letter, one special character and one digit

characters_test=[uppercase_test,lowercase_test,special_test,digits_test]    

length=len(password_input)

strength=0

print("Checking Commonly used passwords...\n")
with open("password_strength\passwordlist.txt",'r') as f:# you can use any other password list , here i am using a list i found on github (https://github.com/danielmiessler/SecLists/blob/c9fbc4350b2e446d9ad16a9d5af94216a98adf40/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt)
    if password_input in f.read().splitlines():
        print("Password found in Common list, Password is too common and can be easily guessed\n")
        exit()
print("Common list check complete!, Password is not in common list\n")
print("Checking Password Strength manually...\n")

if length>8:
    strength+=1
    
if length>12:
    strength+=1
    
if length>16:
    strength+=1

if length>20:
    strength+=1

if sum(characters_test) >1:
    strength+=1    

if sum(characters_test)>2:
    strength+=1
    
if sum(characters_test)>3:
    strength+=1
    
    
if strength < 3:
    print("Password is very weak! :( \n")
    
elif strength ==3:
    print("Password is ok! :| \n")

elif strength >3 and strength <6:
    print("Password is good! \n")

elif strength >6:
    print("Password is very strong!! :) \n")
    
print("Total Password Strength Score: ",strength,"/7 \n")

print("Thank you for using Password Strength Checker! \n")

#Coded by Gaurav Chalil 

    
