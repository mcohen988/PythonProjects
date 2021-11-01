import random
import string

alphabets =  list(string.ascii_letters)
digits = list(string.digits)
special_chars = list("!@#$%^&*()[].-")

def gen_randon_password():
    # Asking the user for password length
    length = int(input("Enter password length: "))
    alphabets_count = int(input("Enter the number of characters you want: "))
    digits_count = int(input("Enter the number of digits you want: "))
    special_chars_count = int(input("Enter the number of special characters you want: "))
    
    overall_count = alphabets_count + digits_count + special_chars_count

    if overall_count > length:
        print("The overall count is greater than the length you choose.")
        return
        
    password = []
        
    # random.choice() returns a random element from the given sequence
    
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))
    
    for i in range(digits_count):
        password.append(random.choice(digits))
        
    for i in range(special_chars_count):
        password.append(random.choice(special_chars))

    # shuffle() takes a sequence and returns the sequence in a random order 
    random.shuffle(password)
    # printing the password
    print("".join(password))

# Calling the function
gen_randon_password()
