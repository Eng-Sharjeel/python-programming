# --> a append mode
# adds data at the end of file

file = open("sample.txt", "a")
file.write("\nThis line is added later")
file.close()
