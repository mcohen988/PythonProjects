import string
import secrets  #used for generating cryptographically strong random numbers

alphabets =  list(string.ascii_letters)
digits = list(string.digits)
special_chars = list("#$%&'()*+,-./:;<=>?@[\]^_`{|}~")

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
        
    # secrets.choice() method return a randomly-chosen element from the given sequence.
    
    for i in range(alphabets_count):
        password.append(secrets.choice(alphabets))
    
    for n in range(digits_count):
        password.append(secrets.choice(digits))
        
    for s in range(special_chars_count):
        password.append(secrets.choice(special_chars))

    # Using the secrets.SystemRandom class, we can use all the functions of a random module
    secrets.SystemRandom().shuffle(password)
    # printing the password
    print("".join(password))

# Calling the function
gen_randon_password()
