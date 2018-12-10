'''
Quickmaths.py: A simple math trainer
Copyright (C) 2018  Hafpaf

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

TODO:
- Run again
- Make different kind of questions
- Print to text file
- Make it run faster on 2nd try
'''
import time
from random import randrange

#generate pseudo-random numbers
number1 = randrange(1,9,1) #Last digit is step
number2 = randrange(1,9,1)

type = input("Choose type: + | - | * | / : ", )
typelist =["+","-","*","/","plus","minus","times","divide"]

#catch answers not within reason
while type not in typelist:
    print("Not a valid answer, try again")
    type = input("Choose type: + | - | * | / : ", )

print("") #make a line break in the terminal output

#The program calculates the answer
sum1 = number1 + number2
sum2 = number1 - number2
sum3 = number1 * number2
sum4 = sum3/number1 #make sure the answer is a whole number.

def init_input():
    if type in ("+","plus"): #works just like type == "+", just with more inputs
        return "What is " + str(number1) + " + " + str(number2) + "?"
    if type in ("-","minus"): #works just like type == "-"
        return "What is " + str(number1) + " - " + str(number2) + "?"
    if type in ("*","times"): #works just like type == "*"
        return "What is " + str(number1) + " * " + str(number2) + "?"
    if type in ("/","divide"): #works just like type == "*"
        return "What is " + str(sum3) + " / " + str(number1) + "?"
    else:
        return "NAN3"

print(init_input()) #print question
#Start timer
time_start = time.time()

#Check if non integer and throw error if not
try:
    number = int(input("Answer: ",))
except ValueError as e:
    print("Not a number") #NaN
    exit()

#End timer
time_end =  time.time()

print(" ")

#Round up timer to 2 decimals.
rounded_number = round(time_end-time_start, 2)
print("Your calculation took", rounded_number, "sec.") # print output

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
    if type in ("/","divide"):
        if number == sum4:
            return time_taken_to_answer()
        else:
            return ("Wrong answer")
    else:
        return ("NaN2")

#Check time taken to answer
def time_taken_to_answer():
    if type in ("+","plus"):
        if rounded_number > 3:
            return "Correct, but too slow"
        elif rounded_number <= 3:
            return "Very nice"
    if type in ("-","minus"):
        if rounded_number > 4:
            return "Correct, but too slow"
        elif rounded_number <= 4:
            return "Very nice"
    if type in ("*","times"):
        if rounded_number > 5:
            return "Correct, but too slow"
        elif rounded_number <= 5:
            return "Very nice"
    if type in ("/","divide"):
        if rounded_number > 7:
            return "Correct, but too slow"
        elif rounded_number <= 7:
            return "Very nice"
    else:
        return None

print(check_answer())
exit()
