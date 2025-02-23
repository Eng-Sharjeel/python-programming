# Fibonacci series up to a user-defined limit

limit = int(input("Enter the limit for fabonacci serires: "))  # User input for limit

a, b = 0, 1  # Initialize first two Fibonacci numbers

print(a, b, end=" ")  # Print first two numbers on the same line

while True:
    next_fib = a + b  # Calculate next Fibonacci number
    if next_fib > limit:  # Stop if it exceeds the user-defined limit
        break
    print(next_fib, end=" ")  # Print the number in a single line
    a, b = b, next_fib  # Move to the next numbers
