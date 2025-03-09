# Recursive Binary Search
# A recursive function is one that calls itself
# Slicing: Specify the start index and the end index, separated by a colon, to return a part of the string. 
# Example --> [2:5], Get the characters from position 2 to position 5 (not included)
# Slicing --> gives new list 

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]

result = recursive_binary_search(numbers, 7)
verify(result)
