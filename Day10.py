# Day10
# Calculator function
'''def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("ANgeLA", "angela"))

def func_1(text):
    return text + text

def func_2(text):
    return text.title()

output = func_2(func_1("hello"))
print(output)

#Functions with Outputs
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  f"Result: {formated_f_name} {formated_l_name}"

#Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
#or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))

#Already used functions with outputs.
length = len(formatted_name)

#Return as an early exit
def format_name(f_name, l_name):
  """Take a first and last name and format it
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False'''

# Day10 Project: Calculator
def add(n1, n2):
    return n1 + n2
# my_add = add
# print(my_add(2, 3))

def sub(n1, n2):
    return n1 - n2
# my_sub = sub
# print(my_sub(3, 2))

def mul(n1, n2):
    return n1 * n2
# my_mul = mul
# print(my_mul(2, 3))

def div(n1, n2):
    return n1 / n2
# my_div = add
# print(my_div(2, 3))

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
#print(operations["*"](4, 8))
def calculator():
    num1 = float(input("What is your first number: "))
    should_accumulate = True
    while should_accumulate:


        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an Operation: ")
        num2 = float(input("What is the next number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer} or 'n' to start a new calculation.")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
calculator()