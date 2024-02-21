#global variable
number = 1


print("Global variable number is", number)

def scope(number):
    #local variable
    number = 2
    print("Local variable number is", number)

number = input("Enter a number: ")
scope(number)
print("Global variable number is", number)

