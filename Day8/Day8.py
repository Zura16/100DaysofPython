# Day8
'''def greet():
    print("a")
    print("b")
    print("c")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Angela")


def life_in_weeks(years):
    weeks = (90 - years) * 52
    print(f"You have {weeks} weeks left.")

life_in_weeks(56)

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(location = "London", name = "Angela")
#greet_with("Angela", "London")'''

# Day8 Project: Love Score calculator
def calculate_love_score(name1, name2):
    # Convert both names to lowercase to make it case insensitive
    name1 = name1.lower()
    name2 = name2.lower()

    # Combine both names into one string
    combined_names = name1 + name2

    # Count occurrences of letters in "TRUE"
    true_count = 0
    true_count += combined_names.count('t')
    true_count += combined_names.count('r')
    true_count += combined_names.count('u')
    true_count += combined_names.count('e')

    # Count occurrences of letters in "LOVE"
    love_count = 0
    love_count += combined_names.count('l')
    love_count += combined_names.count('o')
    love_count += combined_names.count('v')
    love_count += combined_names.count('e')

    # Combine the counts to form a two-digit love score
    love_score = int(str(true_count) + str(love_count))

    print(f"Your love score is {love_score}")
    return love_score


calculate_love_score("Angela Yu", "Jack Bauer")

# Day8 Project: Caesar Cipher
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {output_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt")
    text = input("Type your message here: ")
    shift = int(input("Type the shift number: "))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    print("Do you want to try again? ")
