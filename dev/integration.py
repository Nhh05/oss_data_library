import zlib
import numpy as np
class PNGProcessor:
    def open_png(self, path):
        path = path

        try:
            with open(path, "rb") as file:
                raw_data = file.read()
        except FileNotFoundError:
            print(f"'{path}' was not found.")
            return
        except Exception as e:
            print(f"other error : {e}")
            return
            
        signature = raw_data[:8]
        print("signature: ",signature)
        raw_data = raw_data[8:]
        if signature!=b'\x89PNG\r\n\x1a\n':
            print("not a valid PNG file.")
            return

        def decode_4(raw_data): 
            byte1 = raw_data[0] << 24
            byte2 = raw_data[1] << 16  
            byte3 = raw_data[2] << 8
            byte4 = raw_data[3]
            return int(byte1|byte2|byte3|byte4)

        chunks = []
        while raw_data:
            data_length = decode_4(raw_data[:4])
            chunk_type = raw_data[4:8] .decode("ascii")
            chunk_data = raw_data[8:8+data_length]
            crc = raw_data[8+data_length:12+data_length]

            chunks.append((chunk_type,chunk_data))

            raw_data = raw_data[12+data_length:]

        for type, data in chunks:
            print("data_type  : ",type,"/ data_length: ",len(data))

        image_data = b""
        for type, data in chunks:
            if type=='IHDR':
                width = decode_4(data[0:4])
                height = decode_4(data[4:8])
                color_type = data[9]
                print(f"Width: {width}, Height: {height}, Color Type: {color_type}")
            elif type == "IDAT":
                image_data += data

        if color_type !=0:
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

        row_size = width+1

        pixels = []
        for y in range(height):
            row = []
            for x in range(width): 
                location = y*row_size + x + 1
                row.append(decompressed_data[location])
            pixels.append(row)

        return pixels
    
    def invert_image_colors(pixels):
        pixels = np.array(pixels)
        min_val = pixels.min()
        max_val = pixels.max()
        
        inverted_pixels = max_val - (pixels - min_val)
        return inverted_pixels.tolist()


#########################
import random
class DataPreprocessor:
    """데이터 변환 및 전처리 클래스"""
    def __init__(self):
        pass

    def shuffle_train_test_data(self, X_data, y_data, train_ratio=0.7, seed=None):
        self.seed = seed
        if seed is not None:
            random.seed(self.seed)

        combined_data = list(zip(X_data, y_data))

        # 데이터 섞기
        random.shuffle(combined_data)

        # 데이터 분리
        X_data, y_data = zip(*combined_data)

        # 학습/테스트 데이터 나누기
        split_index = int(len(X_data) * train_ratio)
        X_train = X_data[:split_index]
        y_train = y_data[:split_index]
        X_test = X_data[split_index:]
        y_test = y_data[split_index:]

        return X_train, y_train, X_test, y_test
    
    def flatten(self,data):
        """다차원 배열을 1차원으로 변환"""
        result = []
        for item in data:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            else:
                result.append(item)
        return result

    def encode(self,labels):
        """라벨을 One-hot 인코딩"""
        num_classes = max(labels) + 1
        one_hot = []
        for label in labels:
            vector = [0] * num_classes
            vector[label] = 1
        return one_hot
    
    def scale_data(self,data): #매서드화
        data_min = min(data) #최솟값
        data_max = max(data) #최댓값
    
        if data_min == data_max:  #최대와 최소가 같을 경우 예외 처리
            return[0.5] * len(data)
        
        else:
            scaled_data = []     #스케일링 된 수를 넣는 리스트

            for k in data:       #데이터를 0과 1사이로 스케일링 하는 코드
                scaled_value = (k - data_min) / (data_max - data_min) 
                scaled_data.append(scaled_value) 

            return scaled_data




##################################
#테스트 코드
# PNGProcessor 클래스 테스트
processor = PNGProcessor()
pixels = processor.open_png("test.png")
print()
print(pixels[:])  # 첫 5행의 픽셀 출력
inverted_pixels = PNGProcessor.invert_image_colors(pixels)
print(inverted_pixels[:])  # 반전된 첫 5행의 픽셀 출력

# DataPreprocessor 클래스 테스트
preprocessor = DataPreprocessor()

X_data = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y_data = [0, 1, 0, 1, 0]

X_train, y_train, X_test, y_test = preprocessor.shuffle_train_test_data(X_data, y_data, train_ratio=0.7, seed=42)
print("X_train:", X_train)
print("y_train:", y_train)
print("X_test:", X_test)
print("y_test:", y_test)

nested_data = [[1, 2], [3, [4, 5]], 6]
flattened_data = preprocessor.flatten(nested_data)
print("preprocessor.flatten(nested_data)", flattened_data)

labels = [0, 1, 2, 0, 1]
one_hot_encoded = preprocessor.encode(labels)
print("preprocessor.encode(labels)",one_hot_encoded)
