# Day9
# Dictionaries, Nesting and the Secret Auction
# To create a dictionary
'''programming_dictionary = {
    "Bug": "An array in a program that prevents the program from running as expected.",
    "function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary['Bug'])
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail


capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin", "Hamburg"],
        "total_visits": 5,
    }
}
print(travel_log["Germany"]["cities_visited"])'''

# Day9 Project: Secret Bidding
name_dictionary = {
    "name": input("What is your name? "),
    "bid": input("What's your bid? $"),

}


bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 100)
        continue
