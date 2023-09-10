"""
SILENT AUCTION PROGRAM
****WELCOME TO THE SILENT AUCTION PROGRAM****
What is your name?
What is your bid?
Are there any other bidders? type 'yes' or 'no'
the winner is ____ with a bid of ___
"""
import os
def bid_winner(bidder_data):
    highest=0
    winner=""
    for i in bidder_data:
        bidder_price=bidder_data[i]
        if bidder_price>highest:
            highest=bidder_price
            winner=i
    print(f"The winner is {winner} with a bid price of {highest}")

bidder_list={}
other_bidders=False
while not other_bidders:
    name=input("What is your name?")
    bid=int(input("What is your bid?"))
    bidder_list[name]=bid
    other=input("Are there any other bidders?").lower()
    if other=='no':
        other_bidders=True
        bid_winner(bidder_list)
    elif other=='yes':
        os.system('cls')