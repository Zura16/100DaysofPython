#Day14
#Project: Higher or Lower

from artforday14 import logo, vs
from game_date_forDay14 import data
import random


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:
    
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    
    print("\n" * 200)
    print(logo)

    
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False

