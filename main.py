import random

questions = globals
answers = globals




# Questions and answers
base_questions = ["Name a fruit.", "Name a country.", "Name a superhero.", "Name a movie."]
base_answers = [
    ["apple", "banana", "orange", "strawberry", "blue berry", "grape", "watermelon","avocado"],
    ["usa", "canada", "japan", "australia", "italy", "china", "britain"],
    ["superman", "spiderman", "batman", "wonder woman"],
    ["titanic", "star wars", "the avengers", "jurassic park"]
]
questions = base_questions
answers = base_answers

def populate_list():
  pass

def how_to_play():
    print('\nHow to play:\nYou an another player will both be given a question')

def play_game():
	# Select a random question
	question_index = random.randint(0, len(questions) - 1)
	question = questions[question_index]
	possible_answers = answers[question_index]
	
	print("Question:", question)
	
	# Shuffle the answers
	random.shuffle(possible_answers)

	# Get user's choice
	user_choice = input("Your answer: ")
	remove_please = user_choice
    
	# Check if the answer is correct
	if user_choice.lower() in possible_answers:
		print ('yes')
		answers.remove(remove_please)
	else:
		print ('no')
        
# Main loop
print('Welcome to Family Game Fight')
know = input("Do you know how to play? (Y/N) ")
if know.lower() == 'y':
    print("Well Get Ready!")
    
if know.lower() == 'n':
    how_to_play()
    
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print("Thank you for playing!")