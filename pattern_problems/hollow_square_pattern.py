'''
***** Hollow Square Pattern *****

For n = 5

*****
*   *
*   *
*   *
*****
'''
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    if(i == 1 or i == rows):
        print("*" * rows, end="")
    else:
        print("*", end="")
        print(" " * (rows - 2), end="")
        print("*", end="")
    print("")

