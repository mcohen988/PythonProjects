# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

from datetime import datetime

currentYear = datetime.now().year

name = input("What's your name? ")
age = int(input("How old are you? "))
time_until_100 = 100 - int(age)

print(name + " You will turn 100 in the year " + str(currentYear + time_until_100))
