#import libs
import random
from replit import clear
from art_higher_lower import logo,vs
from higher_lower_game_data import data

def get_random_account():
  return random.choice(data)

# format the data
def format_data(account):  
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return(f"{account_name},a {account_desc}, from {account_country}")

# Check if user is correct
def check_answer(choice,a_follower,b_follower):
  if a_follower > b_follower:
    return choice == "a"
  else:
    return choice == "b"
    
#Display logo
def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()
  
  while game_should_continue:
# generate A and B using the random function
    account_a = account_b
    account_b = get_random_account()
  
    while account_a == account_b:
      account_b = get_random_account()
 
    print(f"comapere A: {format_data(account_a)}.")
    print(vs)
    print(f"comapere B: {format_data(account_b)}.")
  
# Ask user for a guess 
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

# Get follower count to each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(choice,a_follower_count,b_follower_count)

# clear the screen                                                         
    clear()
    print(logo)
                              
# Give user feedback on their choice
# maintain score and display it

    if is_correct:
      score +=1
      print(f"You're right! Current score is {score}")
    else:
      game_should_continue = False
      print(f"Sorry , that's wrong. Final score is {score} ")

game()

 
    



