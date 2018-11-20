'''
-------------
The goal of the game is to calculate FAST!, not correct, but fast
-------------
'''
import math
import numpy
import time
from threading import Timer

#Start timer
start = time.time()

def check_if_number():
    if int(float(input("Write something: ",))) == True:
        return check_if_number()
    else:
        return "NaN"

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
