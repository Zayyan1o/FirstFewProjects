import random as rd
num = rd.randint(0,21)

for i in range(0,3):

	user = int(input("I've chosen a number. Please try to guess a number from 0 to 25. You have 3 attempts. This is your {} attempt: ".format(i+1)))

	if num == user:
		print("You've guessed the right number\n")
		break
	elif num < user:
		print("You've guessed higher\n")
	elif num > user:
		print("You've guessed lower\n")

print("Your attempts are over. Well Played!\n")




print("The number I chose was", num)
int = input("Enter to exit")
 