import random
import os
clear = lambda: os.system('clear')



logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""



def play_game():
	print(logo)
	def deal_card():
		"""Return random card from deck."""
		cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
		return random.choice(cards)

	def calculate_score(cards):
		if sum(cards) == 21 and len(cards) == 2:
			return 0
		if 11 in cards and sum(cards)>21:
			cards.remove(11)
			cards.append(1)
		return(sum(cards))
			
	# Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.


	def compare(user_score, computer_score):
		#Bug fix. If you and the computer are both over, you lose.
		if user_score > 21 and computer_score > 21:
			return "You went over. You lose 😤"


		if user_score == computer_score:
			return "Draw 🙃"
		elif computer_score == 0:
			return "Lose, opponent has Blackjack 😱"
		elif user_score == 0:
			return "Win with a Blackjack 😎"
		elif user_score > 21:
			return "You went over. You lose 😭"
		elif computer_score > 21:
			return "Opponent went over. You win 😁"
		elif user_score > computer_score:
			return "You win 😃"
		else:
			return "You lose 😤"


	user_cards=[]
	computer_cards=[]
	is_game_over = False



	for _ in range(2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())


	while not is_game_over:
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)
		print(f"{user_cards}  socre::{user_score}")
		print(f"Computer first card is : {computer_cards[0]} ")

		if (user_score == 0 or computer_score == 0 or user_score > 21):
			is_game_over = True
		else:
			user_should_deal =input("Enter 'y' to get another card ,type 'n' to end game: ")
			if user_should_deal == 'y':
				user_cards.append(deal_card())
			else:
				is_game_over = True

	while computer_score !=0 and computer_score < 17 :
		computer_cards.append(deal_card())
		computer_score = calculate_score(computer_cards)



	print(f"   Your final hand: {user_cards}, final score: {user_score}")
	print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
	print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()




	

	

