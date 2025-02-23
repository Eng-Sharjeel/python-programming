'''
🔹 Fibonacci Series Formula:
    F(n)=F(n-1)+F(n-2)
where:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2), for n >= 2

Loop iterates "num_terms" times to generate the Fibonacci sequence.
'''

'''
🔹 Why Use lru_cache?
Caches previously computed Fibonacci values.
Significantly reduces redundant calculations.
Boosts performance from O(2ⁿ) to O(n).
'''

# 🔹 Fibonacci Series using Recursion
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    """Recursive function to return the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Taking user input for the number of terms
num_terms = int(input("Enter the number of terms: "))

# Printing Fibonacci series
print("Fibonacci Series:", end=" ")
for i in range(num_terms):
    print(fibonacci(i), end=" ")
