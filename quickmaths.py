'''
----------------------------------
The goal of the game is to calculate FAST!, not correct, but fast
----------------------------------
TODO:
- Make different kind of questions
- Print to text file
'''
import math
import numpy as np
import time
from random import randrange

#generate random number
number1 = randrange(1,9,1) #Last number is step
number2 = randrange(1,9,1)

type = input("Choose type: +, -, * ", )

input_plus = "+"
input_minus = "-"
input_times = "*"

def init_input():
    if type == "+":
        return "What is " + str(number1) + " " + str(input_plus) + " " + str(number2) + "?"
    if type == "-":
        return "What is " + str(number1) + " " + str(input_minus) + " " + str(number2) + "?"
    if type == "*":
        return "What is " + str(number1) + " " + str(input_times) + " " + str(number2) + "?"

sum1 = number1 + number2
sum2 = number1 - number2
sum3 = number1 * number2

print(init_input())
#Start timer
time_start = time.time()


#print("What is",number1,"+",number2,"?")
#sum1 = number1 + number2

#Check if non integer and throw error if not
try:
    number = int(input("Answer: ",))
except ValueError as e:
    print("NaN")

#End timer
time_end =  time.time()

print(" ")

#Round up timer to 3 decimals.
rounded_number = round(time_end-time_start, 3)
print("Calculation took", rounded_number, "ms.") # print output

#check answer
def check_answer():
    if type == "+":
        if number == sum1:
            return time_taken_to_answer()
        else:
            return ("Wrong answer")
    if type == "-":
        if number == sum2:
            return time_taken_to_answer()
        else:
            return ("Wrong answer")
    if type == "*":
        if number == sum3:
            return time_taken_to_answer()
        else:
            return ("Wrong answer")
    else:
        return ("NaN2")

#Check time taken to answer
def time_taken_to_answer():
    if rounded_number > 3.5:
        return "Correct but too slow"
    elif rounded_number < 3.5:
        return "Your math skill is pretty fast boi"
    else:
        return None

print(check_answer())
exit()
