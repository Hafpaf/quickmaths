# quickmaths

A little game with the goal to calculate simpel math equations fast.

#### Run quickmaths.py to try the Program


## Explanation of the code

### The code includes these libaries:
- time

### Check if non integer and throw error if not
'''
try:
    number = int(input("Write something: ",))
except ValueError as e:
    print("NaN")
'''


#### TODO
Make small random math calculations



#### Ressources used:
- https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python
- https://stackoverflow.com/questions/3309664/python-timer-countdown
- https://docs.python.org/3.5/library/functions.html#round
- https://stackoverflow.com/questions/9522446/why-do-i-get-an-error-when-i-call-intinput-where-input-is-decimal-eg-87-9
- https://stackoverflow.com/questions/379906/how-do-i-parse-a-string-to-a-float-or-int-in-python
- https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
