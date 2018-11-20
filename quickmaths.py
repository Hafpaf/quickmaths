'''
-------------
The goal of the game is to calculate FAST!, not correct, but fast
-------------
'''
import math
import numpy
import time
from threading import Timer

start = time.time()
input("Write something: ",)
end =  time.time()
rounded_number = round(end-start, 4)
print(rounded_number, "ms.")
