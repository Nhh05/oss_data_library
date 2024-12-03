print("="*100)
path = "test.png" #이미지 경로 입력

try: # 파일 읽기 시도
    with open(path, "rb") as file:
        raw_data = file.read()
except FileNotFoundError: # 파일 없음 오류
    print(f"'{path}' was not found.")
    exit()
except Exception as e: #그 외의 에러
    print(f"other error : {e}")
    exit()

signature = raw_data[:8]
print("signature: ",signature)
raw_data = raw_data[8:]
if signature!=b'\x89PNG\r\n\x1a\n':
    print("not a valid PNG file.")
    exit()

print("_"*100)

# 4바이트 바이너리 -> int 로 바꿔주는 함수
def decode_4(raw_data): 
    byte1 = raw_data[0] << 24  # 0~15 ---> 시프트
    byte2 = raw_data[1] << 16  
    byte3 = raw_data[2] << 8
    byte4 = raw_data[3]
    return int(byte1|byte2|byte3|byte4)

chunks = []
while raw_data:
    data_length = decode_4(raw_data[:4])
    chunk_type = raw_data[4:8] .decode("ascii")
    chunk_data = raw_data[8:8+data_length]
    crc = raw_data[8+data_length:12+data_length] #데이터 손상방지라는데 일단은 필요없을지도...

    chunks.append((chunk_type,chunk_data))

    raw_data = raw_data[12+data_length:] #저장한 청크 잘라내기

for type, data in chunks:
    print("data_type  : ",type)
    print("data_length: ",len(data))

print("_"*100)

#IHDR, IDAT 분리, 데이터읽기
image_data = b""
for type, data in chunks:
    if type=='IHDR': #IHDR  청크에서 정보추출 -> 메타데이터 가져오기
        width = decode_4(data[0:4])
        height = decode_4(data[4:8])
        color_type = data[9] #색상 구성 정보 담고있음 (0: 그레이스케일, 2: RGB, 6: RGBA)
        print(f"Width: {width}, Height: {height}, Color Type: {color_type}")
    elif type == "IDAT": #IDAT 청크에서의 데이터
        image_data += data

print("IMAGE_DATA: ", image_data)