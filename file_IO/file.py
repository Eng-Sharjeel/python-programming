file = open("sample.txt", "r")  # Open in read mode
content = file.read()  # Read the entire file
print(content)
file.close()  # Always close the file