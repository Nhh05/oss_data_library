def one_hot_encode(lables, num_classes):
    
    ont_hot = [] # 결과값 저장

    for label in labels:

        vector = [0] *  num_classes 
        vector[label] = 1
        ont_hot.append(vector) # 백터로 된 결과값 리스트에 저장

    return one_hot 

