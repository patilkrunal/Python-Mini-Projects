# The GREAT GUESSING GAME

import random
secretNumber = random.randint(1, 20)
print("The number is between 1 and 20. You have 5 chances. Go ahead.")

for guessTaken in range(1, 6):
	print("Take guess "+ str('guessTaken'))
	guess = int(input())

	if guess < secretNumber:
		print("Your guess is less than expected.")
	elif guess > secretNumber:
		print("Your guess is more than expected.")
	else:
		break

if guess == secretNumber:
	print("Good job! You guessed the number in "+ str(guessTaken) + " guesses")
else:
	print("Try again")