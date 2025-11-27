# https://www.w3schools.com/python/python_casting.asp / https://www.w3schools.com/python/python_scope.asp
# Write a function add(a, b) that returns the sum of the two numbers.
# Ask the user for two numbers (as input), convert them to integers, call the function, and print the result.
    
# Write your code here:
def add(a, b):
    return a + b    

number1 = int(input("Input first number: "))
number2 = int(input("Input second number: "))
result = add(number1, number2)
print("Output:", result)    