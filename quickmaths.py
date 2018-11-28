'''
----------------------------------
The goal of the game is to calculate FAST!, not correct, but fast
----------------------------------
TODO:
- Stop at NaN
- Check answer on calculation
'''
import math
import numpy as np
import time
from random import randrange

number1 = randrange(1,9,1) #Last number is step
number2 = randrange(1,9,1)

print("What is",number1,"+",number2,"?")
sum1 = number1 + number2

#Start timer
start = time.time()

#Check if non integer and throw error if not
try:
    number = int(input("Write something: ",))
except ValueError as e:
    print("NaN")

#End timer
end =  time.time()

#Round up timer to 3 decimals
rounded_number = round(end-start, 3)
print(rounded_number, "ms.") # print output

#Check time taken to answer
def time_taken_to_answer():
    if rounded_number > 5:
        return "Too slow"
    elif rounded_number < 5:
        return "Your math skills is pretty fast boi"
    else:
        return None
print(time_taken_to_answer())
