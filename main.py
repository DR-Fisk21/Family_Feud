import random

questions = globals
answers = globals




# Questions and answers
questions = ["Name a popular fruit.", "Name a popular country.", "Name a popular superhero.", "Name a popular movie."]
answers = [
    ["apple", "banana", "orange", "strawberry", "blue berry", "grape", "watermelon", "avocado"],
    ["usa", "canada", "japan", "australia", "italy", "china", "britain", "ukraine"],
    ["superman", "spider-man", "batman", "wonder woman", "iron man", "hulk", "thor", "the flash"],
    ["titanic", "star wars", "the avengers", "jurassic park", "toy story", "home alone", "die hard", "matrix"]
]


def populate_list():
  pass

def how_to_play():
    print('\nHow to play:\nYou an another player will both be given a question\ntThen if you get it righ you will move on to the next round!\nBut, if you fail you will get a strike, 3 strikes and you lose! ')

def play_game():
	# Select a random question
	question_index = random.randint(0, len(questions) - 1)
	question = questions[question_index]
	possible_answers = answers[question_index]

	#strikes
	player1_strikes = 0
	print(f'Player1: {player1_strikes} strikes')
	print("Question:", question)
	
	# Shuffle the answers
	random.shuffle(possible_answers)

	# Get user's choice
	user_choice = input("Your answer: ")
	
    
	# Check if the answer is correct
	if user_choice.lower() in possible_answers:
		print ('yes')
		answers.remove(user_choice)
	else:
		print ('no')
		player1_strikes +=1
    
# Main loop
print('Welcome to Family Game Fight')
know = input("Do you know how to play? (Y/N) ")
if know.lower() == 'y':
    print("Well Get Ready!")
    
if know.lower() == 'n':
    how_to_play()
    
while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("Thank you for playing!")