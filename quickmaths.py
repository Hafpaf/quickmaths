'''
----------------------------------
The goal of the game is to calculate FAST!
----------------------------------
TODO:
- Run again
- Make different kind of questions
- Print to text file
- Make it run faster on 2nd try
'''
#import math
import numpy as np
import time
from random import randrange

#generate pseudo-random numbers
number1 = randrange(1,9,1) #Last digit is step
number2 = randrange(1,9,1)

def choose_type():
    while True:
        type = input("Choose type: + | - | * : ", )
        if type not in ["+","-","*"]:
            return "try again"
            return True
        if type in ["+","-","*"]:
            return False

input_plus = "+"
input_minus = "-"
input_times = "*"

def init_input():
    if choose_type() == "+":
        return "What is " + str(number1) + " " + str(input_plus) + " " + str(number2) + "?"
    if choose_type() == "-":
        return "What is " + str(number1) + " " + str(input_minus) + " " + str(number2) + "?"
    if choose_type() == "*":
        return "What is " + str(number1) + " " + str(input_times) + " " + str(number2) + "?"

#The program calculates the answer
sum1 = number1 + number2
sum2 = number1 - number2
sum3 = number1 * number2

print(init_input()) #this line prints 3 times!
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

#check answer type and answer
def check_answer():
    if choose_type() == "+":
        if number == sum1:
            return time_taken_to_answer()
        else:
            return ("Wrong answer")
    if choose_type() == "-":
        if number == sum2:
            return time_taken_to_answer()
        else:
            return ("Wrong answer")
    if choose_type() == "*":
        if number == sum3:
            return time_taken_to_answer()
        else:
            return ("Wrong answer")
    else:
        return ("NaN2")

#Check time taken to answer
def time_taken_to_answer():
    if rounded_number > 3.5:
        return "Correct, but too slow"
    elif rounded_number < 3.5:
        return "Very nice"
    else:
        return "I got stopped at time_taken_to_answer()!"
#        return None

print(check_answer())
print(" ")

def run_program_again():
    while True:
        run_again = input("Run again?, y or n: ", )
        if run_again not in ["y","n"]:
            return "not valid answer"
            return True
        if run_again == "y":
            return choose_type()
            return init_input()
            return check_answer()
            return time_taken_to_answer()
        if run_again == "n":
                return exit()
        else:
            return "not within the given answers"
            exit()
print(run_program_again())
