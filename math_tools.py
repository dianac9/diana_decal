def add(a, b):          #Returns the sum of a and b, adds 2 numbers and returns their sum.
    return a + b

def subtract(a, b):     #Returns the difference between a and b, subtracts 2 numbers and returns their difference.
    return a - b

def multiply(a, b):     #Returns the product of a and b, multiplies 2 numbers and returns their product.
    return a * b

def divide(a, b):       #Returns the quotient of a divided by b, divides a by b and returns their quotient. 
    if b == 0:
        return "Error: you can not divide by zero!"
    else:
        return a / b