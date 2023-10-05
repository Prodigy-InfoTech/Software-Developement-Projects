
import random 
import string

len = int(input("Enter the lenght of password:\n")) # takes the length of your password

while True:
    choose = int(input('''Select the combination for your password :
                       a. Enter "1" for Alphanumeric pasword
                       b. Enter "2" for Alphabet + Punctuations in your password
                       c. Enter "3" for Numbers + Punctuations in your password
                       d. Enter "4" for Alphabet + Digits + Punctuations in your password
                       e. Enter "0" to exit
                       Enter your choice: ''')) 
    
    if (choose == 1):
        pass_1 = "".join(random.sample(string.ascii_letters + string.digits,len)) # creates a password containing alphabets and nuumbers only.
        print(f"Your password is: {pass_1}") 
        break
    elif (choose == 2):
        pass_1 = "".join(random.sample(string.ascii_letters + string.punctuation,len))#Creates a password containing alphabets and punctuations only
        print(f"Your password is: {pass_1}")
        break
    elif (choose == 3):
        pass_1 = "".join(random.sample(string.digits + string.punctuation,len))#Creates a password containing numbers and punctuations.
        print(f"Your password is: {pass_1}")
        break
    elif (choose == 4):
        pass_1 = "".join(random.sample(string.ascii_lowercase + string.ascii_uppercase  + string.digits + string.punctuation,len))# Creates a password containing alphabets , numbers and punctuations.
        print(f"Your password is: {pass_1}")
        break
    elif(choose == 0): 
        # print("thank you")
        break
    else:
        print("[ERROR], Invalid Try Again!!! \n ") #thorws an error message when the number is not valid
