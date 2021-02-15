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



____________________________________________________________________________________________________________________
>>> Functions (def) - A block of code that only runs when its called. A function can return data as a result , you can pass data into the function and this is known as a 'parameter': (See more here) https://www.learnpython.org/en/Functions
---------------------------------------------------------------------------------------------------------------------


# A function is declared with the word 'def', followed by the name you choose to use for the function, and then parentheses.- *

def name_of_function():
	pass

# If you declare a function and do not have code written inside of it yet, then simply add pass statement so the it does not cause errors. Pass is just a null statement, see more here > https://www.educative.io/edpresso/what-is-pass-statement-in-python- *


_____________________________________________________________________________________________________________________


---------------------------------------------------------------------------------------------------------------------


# Ex: Make a function return True ( this funciton now also equals True) especially if this is the only thing it does.

def func():
	return True


_____________________________________________________________________________________________________________________



# Info - An entire script 'file.py' carries a global scope and a function carries its own within it. More on scopes here > https://www.w3schools.com/python/python_scope.asp






'''






























# Try it your self......
# Answer all the questions below, then move on to num_guess.py


#1.)print 2 conditions using Comparing operators...


# 2.) print 3 random numbers between 55-89...


# 3.) print the Boolean of 2 random numbers between 1-8 being compared using Comparing operators...:)


# 4.) create a function and add 1-3 inside of it. Call the function.




''' 5.) save 2 random numbers between 15-30 into variables.
 Run an if statement with those 2 variables being compared 
 using Comparing operators as the condition. If True, 
 run "print('This time its true')". If False, 
 run "print('this time its false')"...:)
'''


# 6 .) create a function and add 5 inside of it. Call the function.



