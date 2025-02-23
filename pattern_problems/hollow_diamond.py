'''
****** Hollow Diamond *****
    *    
   * *   
  *   *  
 *     * 
*********

'''
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")  # Print leading spaces
    if i == 1 or i == rows:
        print("*" * (2 * i - 1))  # Print full row of stars for first & last row
    else:
        print("*" + " " * (2 * i - 3) + "*")  # Print stars at the edges with spaces inside
