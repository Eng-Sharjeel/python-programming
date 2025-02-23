# Sum of Natural Numbers
# Example: number = 3 --> 1+2+3 = 6 (Output)

n = int(input("Enter your number: "))

i = 1
sum = 0
while(i<=n):
    sum = sum+i
    i = i+1

print(sum)
