import random

class DataPreprocessor:
    """
    데이터 변환 및 전처리 클래스입니다.

    이 클래스는 데이터 섞기와 학습 데이터 세트 및 테스트 데이터 세트로 분리하는 기능을 제공합니다.
    재현성을 위해 랜덤 시드를 설정할 수 있습니다.
    """

    def __init__(self):
        """
        DataPreprocessor 클래스 초기화 메서드.
        """
        self.seed = None

    def shuffle_train_test_data(self, x_data, y_data, train_ratio=0.7, seed=None):
        """
        데이터를 섞고 학습 데이터 세트 및 테스트 데이터 세트로 분리합니다.
        
        매개변수:
            x_data (list): 섞고 분리할 특징(feature) 데이터.
            y_data (list): 섞고 분리할 타겟(target) 데이터.
            train_ratio (float, optional): 학습 데이터 비율 (기본값: 0.7).
            seed (int, optional): 랜덤 시드 값으로, 설정 시 결과가 재현 가능합니다 (기본값: None).

        리턴값:
            tuple: 네 개의 리스트로 구성된 튜플.
                - train_x (list): 학습 데이터 세트의 특징 데이터.
                - train_y (list): 학습 데이터 세트의 타겟 데이터.
                - test_x (list): 테스트 데이터 세트의 특징 데이터.
                - test_y (list): 테스트 데이터 세트의 타겟 데이터.

        사용예제:
            >>> preprocessor = DataPreprocessor()
            >>> x_data = [1, 2, 3, 4, 5]
            >>> y_data = ['a', 'b', 'c', 'd', 'e']
            >>> train_x, train_y, test_x, test_y = preprocessor.shuffle_train_test_data(x_data, y_data, train_ratio=0.8, seed=42)
        """
        # 랜덤 시드 설정
        self.seed = seed
        if seed is not None:
            random.seed(self.seed)

        # x_data와 y_data를 쌍으로 묶음
        combined_data = list(zip(x_data, y_data))

        # 데이터 섞기
        random.shuffle(combined_data)

        # 다시 x와 y로 분리
        x_data, y_data = zip(*combined_data)

        # 데이터 분리 인덱스 계산
        split_index = int(len(x_data) * train_ratio)
        train_x = x_data[:split_index]
        train_y = y_data[:split_index]
        test_x = x_data[split_index:]
        test_y = y_data[split_index:]

        return train_x, train_y, test_x, test_y
