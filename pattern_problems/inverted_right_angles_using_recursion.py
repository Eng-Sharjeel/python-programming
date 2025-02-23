'''
***** Inverted Right-Angled Triangle *****

For n = 5
*****
****
***
**
*

'''

# using recursion 

def pattern(n):
    if (n == 0):
        return
    print("*" * n)
    pattern(n-1)

pattern(5)
