"""Program to convert temperatures between F and C"""

# define a function to convert F to C
def f_to_c(f_temp):
    """Convert F to C"""
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp

def c_to_f(c_temp):
    """Convert C to F"""
    f_temp = c_temp * 9 / 5 + 32
    return f_temp

def convert_temp(temp, unit):
    """Convert temperature from F to C or C to F"""
    if unit == "F":
        return f_to_c(temp)
    elif unit == "C":
        return c_to_f(temp)
    else:
        return None

# get the temperature from the user
temp = float(input("What is the temperature? "))
unit = input("What is the unit? (F or C) ")


print(f"The converted temperature is {convert_temp(temp, unit):.2f}")
