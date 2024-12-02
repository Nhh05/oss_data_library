path = "test.png"

try:
    with open("test.png","rb") as file:
        binary_data = file.read()
        print(binary_data)
except:
    print(f"'{path}' was not found.")