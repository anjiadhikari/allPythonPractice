import random 
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""


Easy_Level_Turn = 10
Hard_Level_Turn = 5

print(" Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")



def check_answer(guss,answer,turns):
	if guss > answer:
		print("Too High   Guess again \n")
		return turns - 1
	elif guss < answer :
		print("Too Low   Guess again \n")
		return turns - 1
	else:
		print(f'You guess Right! You won Answer is {answer}')
		return 
		


	# Make function to set difficulty

def set_difficulty():
	level = input("Choose a difficulty.Type easy or hard : ")
	if level == "easy":
		return Easy_Level_Turn
	else:
		return Hard_Level_Turn




	#Taking input from user 
def game():
	print(logo)
	actual_number = random.randint(1,100)
	turns=set_difficulty()

	guess =0
	while guess!=actual_number:
		print(f'You have {turns} attempts remaining to guess the number.')
		guess = int(input('Make a Guess: '))
		turns =check_answer(guess,actual_number,turns)

		if turns == 0:
			print("You've run out of guesses, you lose.")
			break



game()

