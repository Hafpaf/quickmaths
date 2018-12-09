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

type = input("Choose type: + | - | * : ", )
typelist =["+","-","*","plus","minus","times"]

#catch answers not within reason
while type not in typelist:
    print("Not a valid answer, try again")
    type = input("Choose type: + | - | * : ", )

print("") #make a line break in the terminal output

input_plus = "+"
input_minus = "-"
input_times = "*"

def init_input():
    if type in ("+","plus"): #works just like type == "+", just with more inputs
        return "What is " + str(number1) + " " + str(input_plus) + " " + str(number2) + "?"
    if type in ("-","minus"): #works just like type == "-"
        return "What is " + str(number1) + " " + str(input_minus) + " " + str(number2) + "?"
    if type in ("*","times"): #works just like type == "*"
        return "What is " + str(number1) + " " + str(input_times) + " " + str(number2) + "?"
    else:
        return "NAN3"

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
    exit()

#End timer
time_end =  time.time()

print(" ")

#Round up timer to 3 decimals.
rounded_number = round(time_end-time_start, 3)
print("Calculation took", rounded_number, "ms.") # print output

#check answer type and answer
def check_answer():
    if type in ("+","plus"):
        if number == sum1:
            return time_taken_to_answer()
        else:
            return ("Wrong answer")
    if type in ("-","minus"):
        if number == sum2:
            return time_taken_to_answer()
        else:
            return ("Wrong answer")
    if type in ("*","times"):
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
        return None

print(check_answer())
exit()
