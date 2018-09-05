"""
start
"""
from random import randint
from time import sleep

def get_user_guess():
	guess = int(input("unesi broj: "))
	return guess
def roll_dice(number_of_sides):
	first_roll = randint(1, number_of_sides)
	second_roll = randint(1, number_of_sides)
	max_val = number_of_sides * 2
	print("Maximum value %d" % (max_val))
	guess = get_user_guess()
	if guess > max_val:
		print("invalid guess")
	else:
		print("Rolling...")
		sleep(2)
		print("First roll %d" % (first_roll))
		sleep(1)
		print("Second roll %d" % (second_roll))
		sleep(1)
		total_roll = first_roll + second_roll
		print("Result... %d" % (total_roll))
		sleep(1)
		if guess == total_roll:
			print("You Won!!")
		else:
			print("You Lost")

roll_dice(6)