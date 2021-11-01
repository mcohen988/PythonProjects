import random
import string

alphabets =  list(string.ascii_letters)
digits = list(string.digits)
special_chars = list("!@#$%^&*()")
all = list(string.ascii_letters + string.digits + "!@#$%^&*()")

alphabets_count = int(input("Enter the number of characters you want: "))
digits_count = int(input("Enter the number of digits you want: "))
special_chars_count = int(input("Enter the number of special characters you want: "))
overall_count = alphabets_count + digits_count + special_chars_count

password = "".join(random.sample(all, overall_count)) 
print(password)
