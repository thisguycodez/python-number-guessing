import random
from random import randint

'''
_____________________________________________________________________________________________________________________
>>> If/else statements - is a conditional statement that runs code depending on whether an expression is true or false:
---------------------------------------------------------------------------------------------------------------------



* if - the statement that will allow code ITS HOLDING to run if the condition is True
-----------------------------------------------------------------------------------
if 1 == 1:
	print('this code is running because 1 is equal to 1',True)


print('this code will run regardless. Its not apart of the if statement')

___________________________________________________________________________________








* elif - this statement will allow code ITS HOLDING to run if the condition is True and if the 'If' statement before it was False.

-----------------------------------------------------------------------------------


# statement checked 1st
if 1 > 2:
	print('this code is running because 1 is GREATER than 2',True)

# statement checked if 1st statement is false
elif 1 < 2:
	print('this code is running because 1 is LESS than 2',True)

___________________________________________________________________________________







* else - the statement that will allow code ITS HOLDING to run if no other statement before it was True (if,elif).

-----------------------------------------------------------------------------------

# statement checked 1st
if 100 < 0:
	print('this code is running because 100 is less than 0',True)

# statement checked if 1st statement is false
elif 100 < 50:
	print('this code is running because 1 is LESS than 2',True)

# statement checked if all statements before this were also false
else:
	print('this will run by default....ELSE')
___________________________________________________________________________________


_____________________________________________________________________________________________________________________
>>> Random Module (random) - Used for random value returns from a list(array) or generates random numbers based on ranges given as arguements(parameters). We Will only use the 'randint' method built into this module: See More Here: https://docs.python.org/3/library/random.html
---------------------------------------------------------------------------------------------------------------------


* - import this module into your script.- *
* - We are only using 'randint' so this Can be imported in different ways - *





* 1....just pull the method its self out alone
_____________________________________________________________________________________________________________________

from random import randint

# prints a random number between 1-100
print(randint(1,100))

---------------------------------------------------------------------------------------------------------------------






* 2....pull the method its self out alone and rename it to whatever you want 'rando'
_____________________________________________________________________________________________________________________

from random import randint as rando

# prints a random number between 1-100
print(rando(1,100))

---------------------------------------------------------------------------------------------------------------------





* 3....import random and use the method randInt as the 'random' modules attribute
_____________________________________________________________________________________________________________________

import random

# prints a random number between 1-100
print(random.randint(1,100))

---------------------------------------------------------------------------------------------------------------------










'''






























# Try it your self......
# Answer all the questions below, then move on to test3.py


# 1.) print 3 random numbers between 55-89...


# 2.) print the Boolean of 2 random numbers between 1-8 being compared using Comparing operators...:)


''' 3.) save 2 random numbers between 15-30 into variables.
 Run an if statement with those 2 variables being compared using
  Comparing operators as the condition. If True,
   run "print('This time its true')". 
   If False, run "print('this time its false')"...:)
'''




