'''
Problem:
Find the Greatest Common Divisor (GCD) of two numbers using recursion.

🔹 Mathematical Formula (Euclidean Algorithm):
    GCD(a,b) = GCD(b,a mod b)

Base case: If b == 0, return a.
'''

def gcd(a, b):
    if b == 0:  # Base case
        return a
    return gcd(b, a % b)  # Recursive case

print(gcd(48, 18))  # Output: 6

'''
Dry Run:

gcd(48, 18) = gcd(18, 48 % 18) → gcd(18, 12)
gcd(18, 12) = gcd(12, 18 % 12) → gcd(12, 6)
gcd(12, 6) = gcd(6, 12 % 6) → gcd(6, 0)
gcd(6, 0) = 6 (Base case reached)


'''