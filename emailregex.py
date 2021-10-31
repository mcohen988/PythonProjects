import re

valid = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
    
    if(re.search(valid, email)):
        return "Valid email"

    else:
        return "Invalid Email"
 
 
# Testing the code

emails = [
    "test@example.com",
    "valid@gmail.com",
    "invalid@gmail",
    "invalid",
    "not an email",
    "invalid@email",
    "!@/",
    "test@@example.com",
    "test@.com",
    "test@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@exam!ple.com",
    "moshe@walla.co.il",
    "MOSHE@GMAIL.COM",
    "MOSHE.J@GMAIL.COM",
    "MOSHE-J@your-earth.uk",
    "david@walla.co.uk",
    "no-reply@test.com"
]

for email in emails:
    print(check(email))
    