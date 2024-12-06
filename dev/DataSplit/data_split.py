
import random

class FisherYatesShuffler2D:
    def __init__(self, seed=None):
        
        self.seed = seed
        if seed is not None:
            random.seed(seed)

    def shuffle_rows(self, data):
        
        random.shuffle(data)  # 행 순서 섞기
        return data

    def set_seed(self, seed):
        
        self.seed = seed
        random.seed(seed)

    def split_data(data, train_ratio=0.7):
    
        split_index = int(len(data) * train_ratio)
        train_data = data[:split_index]
        test_data = data[split_index:]
        return train_data, test_data

 
