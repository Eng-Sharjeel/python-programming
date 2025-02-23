# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping without third variable
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
