path = "test.png" #이미지 경로 입력

try:
    with open(path,"rb") as file:
        raw_data = file.read()
        print(raw_data)
except:
    print(f"'{path}' was not found.")


signature = raw_data[:8]
raw_data = raw_data[8:]
if signature!=b'\x89PNG\r\n\x1a\n':
    print("not a valid PNG file.")
    exit()


chunks = []
while raw_data:
    byte1 = raw_data[0] << 24  # 0~15 ---> 시프트
    byte2 = raw_data[1] << 16  
    byte3 = raw_data[2] << 8
    byte4 = raw_data[3]
    data_length = int(byte1|byte2|byte3|byte4) #한 청크의 데이터 길이를 찾음
    chunk_type = raw_data[4:8] .decode("ascii")
    chunk_data = raw_data[8:8+data_length]
    crc = raw_data[8+data_length:12+data_length] #데이터 손상방지라는데 일단은 필요없을지도...

    chunks.append((chunk_type,chunk_data))

    raw_data = raw_data[12+data_length:] #저장한 청크 잘라내기

print(chunks)

    
    