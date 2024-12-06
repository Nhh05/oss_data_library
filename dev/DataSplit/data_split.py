import random

class DataPreprocessor:
    """데이터 변환 및 전처리 클래스"""
    def __init__(self):
        self.seed = None

    def shuffle_train_test_data(self, x_data, y_data, train_ratio=0.7, seed=None):
       
        # 랜덤 시드 설정
        self.seed = seed
        if seed is not None:
            random.seed(self.seed)

        # x_data와 y_data를 짝으로 묶음
        combined_data = list(zip(x_data, y_data))

        # 데이터 섞기
        random.shuffle(combined_data)

        # 다시 x와 y로 분리
        x_data, y_data = zip(*combined_data)

        # 데이터 분리
        split_index = int(len(x_data) * train_ratio)
        train_x = x_data[:split_index]
        train_y = y_data[:split_index]
        test_x = x_data[split_index:]
        test_y = y_data[split_index:]

        return train_x, train_y, test_x, test_y
