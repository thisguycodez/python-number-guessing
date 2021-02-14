# Learning Python With Projects (Number guessing) 
> Syntax - Comments, Prints, Variables, Strings, Integers, String Concatenations, Inputs, Comparison operators, and if/else statements.

> https://youtu.be/Wtz_jYVf2p0


## Tutorial
	    
___
#### test1.py file

> Comparison operators - Used to return results 'True or False' depending on the condition(values being compared):	


*  Greater than (>) True if left operand is greater than the right...example below will return True (opposite will return False)

```python
#True
print(2 > 1)
```

*  Less than (<) True if right operand is greater than the left...example below will return True (opposite will return False) 

```python
#True
print(1 < 2)
```

*  Equal to (==) True if both operand...example below will return True (opposite will return False) 

```python
#True
print(1 == 1)
```

*  Greater Than or Equal to(>=) True if left operand is greater than or equal to the right...example below will return True (the opposite will return False) 

```python
#True
print(2 >= 2)
```
```python
#False
print(3 >= 2)
```
*  Less Than or Equal to(<=) True if left operand is less than or equal to the right...example below will return True (opposite will return False)

```python
#True
print(3 <= 3)

#False
print(1 <= 3)
```

___

#### test2.py file

> If/else statements - is a conditional statement that runs code depending on whether an expression is true or false:

* if - the statement that will allow code it holds, to run if the condition is True

```python
if 1 == 1:
	print('this code is running because 1 is equal to 1',True)


print('this code will run regardless. Its not apart of the if statement')
```
* elif - this statement will allow code it holds, to run if the condition is True and if the 'If' statement before it was False.

```python
# statement checked 1st
if 1 > 2:
	print('this code is running because 1 is GREATER than 2',True)

# statement checked if 1st statement is false
elif 1 < 2:
	print('this code is running because 1 is LESS than 2',True)
```


* else - the statement that will allow code it holds to run if no other statement before it was True (if,elif).

```python
# statement checked 1st
if 100 < 0:
	print('this code is running because 100 is less than 0',True)

# statement checked if 1st statement is false
elif 100 < 50:
	print('this code is running because 1 is LESS than 2',True)

# statement checked if all statements before this were also false
else:
	print('this will run by default....ELSE')
```

___


> 3. Random Module (random) - Used for random value returns from a list(array) or generates random numbers based on ranges given as arguements(parameters). We Will only use the 'randint' method built into this module: See More Here: https://docs.python.org/3/library/random.html


* - import this module into your script.- *
* - We are only using 'randint' so this Can be imported in different ways - *


* 1....just pull the method its self out alone

```python
from random import randint

# prints a random number between 1-100
print(randint(1,100))
```
* 2....pull the method its self out alone and rename it to whatever you want 'rando'
```python
from random import randint as rando

# prints a random number between 1-100
print(rando(1,100))
```

* 3....import random and use the method as the 'random' modules attribute
```python
import random

# prints a random number between 1-100
print(random.randint(1,100))
```

___

#####Try writing the syntax in try.py

```python

# Try it your self......
# Answer all the questions below, then move on to num_guess.py


#1.)print 2 conditions using Comparing operators...


# 2.) print 3 random numbers between 55-89...


# 3.) print the Boolean of 2 random numbers between 1-8 being compared using Comparing operators...:)


''' 4.) save 2 random numbers between 15-30 into variables. Run an if statement with those 2 variables being compared using Comparing operators as the condition. If True, run "print('This time its true')". If False, run "print('this time its false')"...:)
'''
```

___

> # Number Guessing Project - Follow and apply each step.
  

```python 

# 1.) Import everything you need, remember we will be using randint attribute from the random module....
from random import randint as rando

# 2.) Save the random number into a variable - range should be from 1-100 or over
hidden_num = rando(1, 100)


# 3.) Create and intro using prints (Optional)
print(colors.cyan,'________________________ThisGuyCodez_________')
print(colors.red,'____0__________3____________9___3_______2____')
print(colors.red,'_1________5_________6______2________11______7')
print(colors.red,'_____12__________8______1_________4__________')
print(colors.red,'3_________5________2______0____77______6_____24')
print(colors.red,'____0__________3____________9___________2____')
print(colors.cyan,'_________Python_Number_guessing_Game_________\n\n')


# 4.) Create your function to use a scope for your game and easy for a 'reset button'(recall function for the game to run again)


''' 
5a.) Compare number to hidden_num,high,low,and the difference from the hidden_num.

5b.) If the guessed_num is correct then ask user if they'd like to play again, if not - end it.

5c.) If it is not the right guessing number, print the relevant message and return your function to run again.
'''



```
___


> *CONGRATS YOU JUST PROGRAMMED YOUR A Number Guessing GAME IN PYTHON*
---
> *SEE HOW FAR YOU CAN GO AN SHARE IN THE COMMENTS*


### Thanks For Reading 
