import re

valid = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
    
    if(re.search(valid, email)):
        print(email + " is valid")

    else:
        print(email + " is invalid")
 
 
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
    "no-reply@test.com",
    "no+reply@test.co.il"
]

for email in emails:
    check(email)
