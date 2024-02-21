"""Examples of creating functions in Python."""

# define a function with no parameters and no return value
def say_hello():
    print("Hello World!")

# define a function with one parameter and no return value
def say_hello_to(name):
    print("Hello", name)

# define a function with one parameter and a return value
def get_user_name(prompt):
    return input(prompt)

# define a function with two parameters and a return value
def calculate_total(price, tax_rate):
    total = price + (price * tax_rate)
    return total

# call the functions

# call a function with no arguments
say_hello()

# call a function with one argument
say_hello_to("Ed")



# call a function saving the return value
userName = get_user_name("What is your name? ")
print("Hello", userName)

# call a function and pass the return value to another function
itemPrice = float(input("What is the price? "))

# call a function with two arguments and pass the return value
print(f"The total price with tax is {calculate_total(itemPrice, 0.06):.2f}")
