from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

finish = False
bidder= {}

def find_highest_bidder(bidding_record):
  highest_bid = 0                     
  for key in bidding_record:
    bid_amount = bidding_record[key]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = key
  print(f"The winner is {winner} with a bid of {highest_bid}")

while not finish:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidder[name]=bid
  decision = input("Are there any other bidders? Type 'yes' or 'no'.")
  if decision == "no":
    finish = True
    find_highest_bidder(bidder)
  elif decision == "yes":
    clear()

 
      


  
    
  