from random import randint




class colors:
	black='\033[30m'
	red='\033[31m'
	green='\033[32m'
	orange='\033[33m'
	blue='\033[34m'
	purple='\033[35m'
	cyan='\033[36m'
	lightgrey='\033[37m'
	darkgrey='\033[90m'
	lightred='\033[91m'
	lightgreen='\033[92m'
	yellow='\033[93m'
	lightblue='\033[94m'
	pink='\033[95m'
	lightcyan='\033[96m'


print(colors.red,'____24___________________ThisGuyC0dez_______0_')
print(colors.lightblue,'____0__________3____________9___3_______2____')
print(colors.lightgreen,'_1________5_________6______2________11______7')
print(colors.lightblue,'_____12__________8______1_________4__________')
print(colors.lightgreen,'3_________5_____2_____0______77______6_____24')
print(colors.lightblue,'____0________123____________9___________2____')
print(colors.yellow,'_________Python_Number_guessing_Game_________\n\n')








def game():
	'''
	1.) Create variables holding the "low" number , "high" number ,
	 and 'hidden' number.
	'''
	low = 1
	high = 100


	hidden = randint(low, high)

	''' 
	str.isnumeric()

	2.)
	-Get the users guessed number and save it to a variable
	-Use if/else statements to make sure its an integer
	-If its not then restart game.
	'''
	def ask_4_num():
		# color change
		print(colors.yellow)
		guessed_num = input(f"Guess a number between {low} and {high}\n\n")



		# using .isnumeric() to check if string only holds numbers
		if guessed_num.isnumeric():

			# use the int method to change string data type into integer
			guessed_num = int(guessed_num)

		else:

			print(colors.red,'That is not a number...')
			return ask_4_num()





			
		''' 
		3.)
		- See if the number guessed by the user is correct 1st. If correct,
		 then print a congratulating message and end game . (Or prompt for a restart)

		- If the guessed number is wrong then print out 
		a message explaining how wrong the guess is. (Restart Game)

		- Use if elif and else statements accurately to catch all possibilities
		'''


		# if the user won the game....
		if guessed_num == hidden:
			print(colors.green,f"Nice!! You guessed {hidden} right!!")


			# ask to play again
			play_again = input('Want to play again? Yes(y) No(n)')

			# if user wants to play again
			if 'y' in play_again.lower():
				print(colors.blue,'Restarting Game.....')

				# restart game
				return game()

			else:
				print(colors.red,'Ending Game.')
				return True


		# if guess is out of range
		elif guessed_num < low or guessed_num > high:
			print(colors.purple,'That number is out of range....')

			# ask again
			return ask_4_num()


		# if guess is too low
		elif guessed_num < hidden:
			print(colors.blue,'That number is too low...')

		# if guess is too high or any other answer thats not wanted...
		else:
			print(colors.blue,'That number is too high...')
			

		
		return ask_4_num()



	return ask_4_num()


# run program...
game()

