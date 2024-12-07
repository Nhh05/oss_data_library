from DataPreProcessor import DataPreProcessor

X_data = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
y_data = [0, 1, 0]

processor = DataPreProcessor()

# 데이터 섞기, 분리
X_train, y_train, X_test, y_test = processor.shuffle_train_test_data(X_data, y_data, train_ratio=0.75, seed=42)
print("Train Data  :", X_train, y_train)
print("Test Data   :", X_test, y_test)
#flatten ()
flat_data = processor.flatten(X_train)
print("flat_data   : ", flat_data)

# 데이터 스케일링
scaled_data = processor.scale_data(X_train)
print("scaled_data : ", scaled_data)

# 원-핫 인코딩 사용
encoded_data = processor.encode(y_data)
print("encoded_data: ", encoded_data)
