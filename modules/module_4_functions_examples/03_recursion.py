"""Program to demonstrate recursion in Python using the Fibonacci sequence."""

# define a function to calculate the nth Fibonacci number
def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    # base case
    if n == 1 or n == 2:
        return 1
    # recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# call the function
fib = int(input("What Fibonacci number do you want?"))
print(fibonacci(fib))


