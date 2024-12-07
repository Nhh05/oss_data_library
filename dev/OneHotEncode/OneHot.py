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
    """
    라벨을 원-핫 벡터로 인코딩하는 클래스.

    메서드:
        encode(labels):
            주어진 라벨 리스트를 원-핫 벡터로 인코딩합니다.
    """
    
    def encode(self, labels):
        """
        주어진 라벨을 원-핫 벡터로 변환합니다.

        Args:
            labels (list of int): 인코딩할 정수형 라벨 리스트.

        Returns:
            list of list of int: 원-핫 벡터로 변환된 리스트.

        예제:
            >>> encoder = OneHotEncoder()
            >>> encoder.encode([0, 1, 2])
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        """
        num_classes = max(labels) + 1 # 라벨을 입력하면 넘클래스 자동 생성
        one_hot = [] # 결과값 저장
        for label in labels: 
            vector = [0] * num_classes
            vector[label] = 1
            one_hot.append(vector) # 백터로 된 결과값 리스트에 저장
        return one_hot


# Test
"""encoder = OneHotEncoder()
labels = [0, 1, 2, 3, 5, 8]
print(encoder.encode(labels))"""



