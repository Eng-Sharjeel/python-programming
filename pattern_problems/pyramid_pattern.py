'''
***** Pyramid Pattern ***** 

For n = 5
    *
   ***
  *****
 *******
*********    

'''

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("*" * (2* i - 1), end="")
    print("")


