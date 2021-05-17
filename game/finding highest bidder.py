import os
clear = lambda: os.system('clear')



logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids= {}
bidding_finished = False



#function for finding hihest bidder
def find_highest_bidder(bidding_record):
	highest_bid = 0
	for bidder in bidding_record:
		bid_amount = bidding_record[bidder]
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner =bidder
	print(f"The winner is {winner} with bid amount ${highest_bid}")
		 





while not bidding_finished:
	name = input('Enter the name of bidder : ')
	price =int(input("What is your bid?  $"))

	#adding both key and value to dic
	bids[name]=price
	should_continue = input('Are are there any others bidders? Type   yes or no . ').lower()
	if should_continue == 'no':
		bidding_finished = True
		find_highest_bidder(bids)
	elif should_continue == 'yes':
		clear()


