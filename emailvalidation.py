def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-."
    
    # Detecting invalid characters
    for char in string:
        if char not in valid:
            return True
    return False

def is_valid(email):
    if email.count("@") != 1:
        return False
    # Tuple unpacking - prefix, domain
    prefix, domain = email.split("@")
    
    if has_invalid_characters(prefix):
        return False
    
    if has_invalid_characters(domain):
        return False

    if len(prefix) == 0:
        return False

    if domain.count(".") != 1:
        return False

    if domain.endswith("."):
        return True
            
    domain_name, extension = domain.split(".")
    if len(domain_name) == 0 or len(extension) == 0:
        return False
    return True
    

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
    "MOSH@GMAIL.COM"
]

for email in emails:
    if is_valid(email):
        print(email + " is valid")
    else:
        print(email + " is invalid")
        
