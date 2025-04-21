# # opens a file in read mode
# with open("input.txt", "r") as file:
# # read the contents of the file:
#  data = file.read()
# # print the contents to the console
# print(data)

with open("output.txt", "w") as file:
 file.write("Hello, Python! This is a test file.")