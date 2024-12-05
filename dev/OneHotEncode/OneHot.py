"""/def one_hot_encode(labels, num_classes):
    
    one_hot = [] # 결과값 저장

    for label in labels:

        vector = [0] *  num_classes 
        vector[label] = 1
        one_hot.append(vector) # 백터로 된 결과값 리스트에 저장

    return one_hot


#test
a = [0, 1, 2 ,3, 5, 8]
print(one_hot_encode(a, 9)) """

# 객체로 생성
class OneHotEncoder:
    def encode(self, labels):
        num_classes = max(labels) + 1 # 라벨을 입력하면 넘클래스 자동 생성
        one_hot = []
        for label in labels:
            vector = [0] * num_classes
            vector[label] = 1
            one_hot.append(vector)
        return one_hot


# Test
encoder = OneHotEncoder()
labels = [0, 1, 2, 3, 5, 8]
print(encoder.encode(labels))



