import string

alphabets = string.ascii_letters
key = int(input("Choose the number to shift by: "))

def caesar(text, key):
    # Index slicing by the key the user has choosen
    shifted_alphabets = alphabets[key:] + alphabets[:key]
    # Translation table from the alphabet to the shifted alphabet 
    table = str.maketrans(alphabets, shifted_alphabets)
    return text.translate(table)

# Calling the function
print(caesar("Attack at Dawn", key))