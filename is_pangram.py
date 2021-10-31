# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string

def is_pangram(s):
    az = "abcdefghijklmnopqrstuvwxyz"
    for char in az:
        if char not in s.casefold():
            return False
    return True