try:
    with open("inputidi.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")