from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_the_highest_bits(highest_bists):
    highest_price=0
    winner = ""
    for score in highest_bists:
        bid_amount = int(highest_bists[score])
        if bid_amount>highest_price:
            highest_price = bid_amount
            winner = score
    print(f"The winner is {winner} with a bid of ${highest_price}")

while not bidding_finished:
    name = input("What is your name?:")
    price = input("What is your bid?: $")
    bids[name]=price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_the_highest_bits(bids)
    else:
        print("\n"*100)
