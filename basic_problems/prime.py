n = int(input("Enter your number: "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not Prime")
        break
else:
    ("Number is prime")