import art

print(art.logo)
# TODO-1: Ask the user for input
biders={}
doContinue = True
while doContinue:
    user_name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    # TODO-2: Save data into dictionary {name: price}
    biders[user_name] = bid
    # TODO-3: Whether if new bids need to be added
    choice = input("Are there any other bidders? Type 'yes' or 'no'.")
    if choice == 'no':
        doContinue = False
    elif choice == 'yes':
        doContinue = True
        print("\n" * 20)
    else:
        print("Invalid input. Ending here")
# TODO-4: Compare bids in dictionary
maxBid = 0
bidderName = ""
for b in biders:
    if biders[b] > maxBid:
        maxBid = biders[b]
        bidderName = b

print(f"The winner is {bidderName} with a bid of {maxBid}")



