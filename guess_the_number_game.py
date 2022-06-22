from art_guess_the_number import logo
from random import randint

# Global Variables
easy_turns = 10
hard_turns = 5

# This function is used to find the difficulty level and assign number of turns
def set_difficulty():
  choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if choice == "easy":
    return easy_turns
  elif choice == "hard":
    return hard_turns
  
# This function is used to compare the answer with the guess
def check_answer(answer,guess,turns):  
  if guess > answer:
    print("Too high")
    turns -= 1
    return turns
  elif guess < answer:
    print("Too low")
    turns -= 1
    return turns
  else:
    print(f"You guessed it right!! Your number is {answer} .")
  

# The game starts from here
def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  answer = random.randint(1,100)
  #print(f"Psst, the correct answer is {answer}")
  
  turns = set_difficulty()
 
 
  guess = 0 
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(answer,guess,turns)
    
    if turns == 0:
      print("You fininshed your turns. You lost!")
      return
    elif guess != answer:
      print("Guess again.")
  
game()
