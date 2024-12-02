path = "test.png" #이미지 경로 입력

try:
    with open(path,"rb") as file:
        binary_data = file.read()
        print(binary_data)
except:
    print(f"'{path}' was not found.")