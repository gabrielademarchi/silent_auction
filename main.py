import os
from art import logo
def clear(): return os.system('cls')


more_bids = True

print(logo)
print('Welcome to the silent auction program.')


def highest_bid(bids):
    highest_bid = 0
    bidder_name = ""
    for keys in bids:
        bid_amount = bids[keys]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            bidder_name = keys
    print(f'The winner is {bidder_name} with a bid of ${highest_bid}')


bids = {}
while more_bids:
    name = input('What is your name?: ')
    bid = int(input('What\'s your bid?: $'))

    bids[name] = bid

    next_bidder = input("Are there any other bidders? Type 'yes' or 'no' ")
    if next_bidder == 'no':
        more_bids = False
        clear()
        highest_bid(bids)
    else:
        clear()
