import random

number = random.randint(1,9)
guess = 0
numOfGuesses = 0

while guess != number and guess != "exit":
	guess = input("What is your guess? ")
	
	if guess == "exit":
		break
		
	guess = int(guess)
	numOfGuesses += 1
	
	if guess < number:
		print("Too low!")
	elif guess > number:
		print("Too high!")
	else:
		print("Congratulations, you got it!")
		print("It took ",numOfGuesses,"tries!")