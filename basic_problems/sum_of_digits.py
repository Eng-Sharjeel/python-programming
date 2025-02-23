'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3 
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + ... + n - 1 + n
sum(n) = sum(n-1) + n
'''
# using recursion 

def sum_of_n (n):
    if(n == 1):
        return 1
    return sum_of_n (n - 1) + n

print(sum_of_n (4))