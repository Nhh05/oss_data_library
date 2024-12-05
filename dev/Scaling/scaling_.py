def scale_data(data): #매서드화
    
    data_min = min(data) #최솟값
    data_max = max(data) #최댓값
   
    if data_min == data_max:  #최대와 최소가 같을 경우 예외 처리
        return[1/data_min] * len(data)
    
    else:
        scaled_data = []     #스케일링 된 수를 넣는 리스트

        for k in data:       #데이터를 0과 1사이로 스케일링 하는 코드
            scaled_value = (k - data_min) / (data_max - data_min) 
            scaled_data.append(scaled_value) 

        return sorted(scaled_data)

