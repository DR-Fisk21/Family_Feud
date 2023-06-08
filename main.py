import random

questions = globals
answers = globals

player1_strikes = 0
player2_strikes = 0

# Questions and answers
questions = ["Name a popular fruit.", "Name a popular country.", "Name a popular superhero.", "Name a popular movie.", "Name a popular video game", "Name a popular kids TV show", "Name a classic Monster", "Name a populer ememy from the TV show 'doctor who'"]
answers = [
    ["apple", "banana", "orange", "strawberry", "blue berry", "grape", "watermelon", "avocado"],
    ["usa", "canada", "japan", "australia", "italy", "china", "britain", "ukraine"],
    ["superman", "spider-man", "batman", "wonder woman", "iron man", "hulk", "thor", "the flash"],
    ["titanic", "star wars", "the avengers", "jurassic park", "toy story", "home alone", "die hard", "matrix"],
    ["minecraft", "sonic", "doom", "super mario", "assassin creed", "hitman", "tetris", "five nights at freddys" ],
    ["thomas & friends", "power rangers", "pingu", "peppa pig", "bluey", "auther", "sesame street", "octonauts"],
    ["vampire", "werewolf", "mummy", "zombie", "big foot", "ghost", "frankensteins monster", "the invisible man"],
	["cybermen", "dalek", "sontaran", "weeping angels", "the master", "auton", "silurian", "ice warriors"]
]

def how_to_play():
    print("\nHow to play:\nYou an another player will both be given a question\nThen you will have to guess one of 8 populer answer to the question if you\n guess wrong you will get a strike. You can't guess the same answer twice.\nthree strikes and your out. (Human error will not be tolerated)")



def play_game():
	# Select a random question
	question_index = random.randint(0, len(questions) - 1)
	question = questions[question_index]
	possible_answers = answers[question_index]

    # Asking the question
	print("\nPlayer 1", question)
	
	# Shuffle the answers
	random.shuffle(possible_answers)

	# Get user's choice
	user_choice = input("Your answer: ")
	
    
	# Check if the answer is correct
	if user_choice.lower() in possible_answers:
		print ('Correct')
		answers[question_index].remove(user_choice.lower())
		#print(answers)
	else:
		print ('Sorry not on the list')
		global player1_strikes
		player1_strikes +=1
		print (f'Player1: {player1_strikes} strikes')

    #player2's turn
	print("\nPlayer 2", question)
	
	# Shuffle the answers
	random.shuffle(possible_answers)

	# Get user's choice
	user_choice = input("Your answer: ")
	
    
	# Check if the answer is correct
	if user_choice.lower() in possible_answers:
		print ('Correct')
		answers[question_index].remove(user_choice.lower())
		#print(answers)
	else:
		print ('Sorry not on the list')
		global player2_strikes
		player2_strikes +=1
		print (f'Player2: {player2_strikes} strikes')

	#check gameover	
	if player1_strikes == 3:
		gameover()
	elif player2_strikes == 3:
		gameover()

# Intro
def intro():
	global player1_strikes
	player1_strikes = 0
	global player2_strikes
	player2_strikes = 0
	print('Welcome to Family Game Fight')
	know = input("Do you know how to play? (Y/N) ")
	if know.lower() == 'y':
		print("Well Get Ready!")
	if know.lower() == 'n':
		how_to_play()

#End of game
def ad():
	print("\nWell then I guess it's time for an ad break,")
	print("See you next time on...")
	print("Family Game Fight! duh duh duh duh duh! *Clapping in the background*")
	ad = input("")
	print('Want a break from the ads?\nget ultra premium spotifly 5-gold++ ultimate 7 deluxe edition')
	exit = input()

#Game over (When someone gets three strike)
def gameover():
	print()
	if player1_strikes == 3:
		print("Player 2 You have won!")			
	elif player2_strikes == 3:
		print("Player 1 You have won!")
	print()
	play_again = input("Do you wish to play again? (Y/N) ")
	if play_again.lower() == "y":
		intro()
	else:
		ad()
		quit()
        
#Start the Game
intro()
#Game Loop
while True:
	play_game()