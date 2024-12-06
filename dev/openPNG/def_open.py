import zlib

def open_png(path):
    path = path

    try: # 파일 읽기 시도
        with open(path, "rb") as file:
            raw_data = file.read()
    except FileNotFoundError: # 파일 없음 오류
        print(f"'{path}' was not found.")
        return
    except Exception as e: #그 외의 에러
        print(f"other error : {e}")
        

    signature = raw_data[:8]
    print("signature: ",signature)
    raw_data = raw_data[8:]
    if signature!=b'\x89PNG\r\n\x1a\n':
        print("not a valid PNG file.")
        return

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
        print("data_type  : ",type,"/ data_length: ",len(data))

    #IHDR, IDAT 분리, 데이터읽기
    image_data = b""
    for type, data in chunks:
        if type=='IHDR': #IHDR  청크에서 정보추출 -> 메타데이터 가져오기
            width = decode_4(data[0:4])
            height = decode_4(data[4:8])
            color_type = data[9] #색상 구성 정보 담고있음 (0: 그레이스케일, 2: RGB, 6: RGBA)
            print(f"Width: {width}, Height: {height}, Color Type: {color_type}")
        elif type == "IDAT": # 여러개의 IDAT 청크 데이터 합치기
            image_data += data

    # PNG 파일을 해석할 수 있는지 미리 확인하기
    if color_type !=0: #color_type 0 만 구현된 상태이기 때문에 제한.
        print(f"PNG '{path}' 파일에서 문제가 발생했습니다.")
        print("그레이스케일(0)번 이외의 png 형식은 아직 구현되지 않았습니다.")
        print("버전 업데이트를 기다려주세요!")
        return
    if image_data==b"":
        print(f"PNG '{path}'IDAT 청크를 발견하지 못했습니다.")
        return

    try:
        decompressed_data = zlib.decompress(image_data)
    except:
        print("<zlib> Failed decompressed IDAT data.")
        return

    print("LENGTH of decoded PNG:",len(decompressed_data))

    row_size = width+1 # +1은 항상 모든 행 앞의 filter_type (1byte)

    #zilb 으로 푼 바이너리를 픽셀 형태로 풀기.
    pixels = []
    for y in range(height):
        row = []
        for x in range(width): 
            location = y*row_size + x + 1 #픽셀로 바꿀 위치 계산
            row.append(decompressed_data[location])
        pixels.append(row) #행을 데이터에 추가

    # open 성공
    return pixels

#n차원 배열 1차원으로 만드는 함수
def flatten(data):
    result = []
    for item in data:
        if isinstance(item,list):
            result += flatten(item) #재귀호출로 계속 풀기
        else:
            result.append(item)
    return result

#함수 실행 테스트
result = open_png("test.png")
for row in result:
    print(row)
print(flatten(result))


'''
#사이즈 유지하면서 프린트
print("RESULT :")
for y in pixels:
    for x in y:
        if x<10:
            print("  ",x,end=" ")
        elif x<100:
            print(" ",x,end=" ")
        else:
            print("",x,end=" ")
    print()
'''