'''
***** Right-Angled Triangle (Ascending Stars) *****

For n = 5
*
**
***
****
*****    
'''

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)

