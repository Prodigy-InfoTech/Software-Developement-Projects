
import random 
import string
len = int(input("Enter the lenght of password:\n"))

#Generating password
Password = "".join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, len))
print(f"Your password is: {Password}")