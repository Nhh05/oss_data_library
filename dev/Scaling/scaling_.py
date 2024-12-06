def scale_data(data):
    """
    데이터 리스트를 0과 1 사이의 값으로 스케일링합니다.

    이 함수는 주어진 숫자 데이터 리스트를 최소값을 0, 최대값을 1로 변환하는 
    **최소-최대 스케일링(Min-Max Scaling)**을 수행합니다. 
    모든 값이 동일한 경우에는 0.5로 채워진 리스트를 반환하여 예외를 처리합니다.

    매개변수:
    ----------
    data : list(float 또는 int)
        스케일링할 숫자 값들의 리스트입니다.

    반환값:
    -------
    list(float)
        스케일링된 값들의 리스트로, 값은 0과 1 사이에 있으며 오름차순으로 정렬되어 있습니다.

    동작 방식:
    ----------
    - 각 값 `k`는 아래 공식을 사용해 스케일링됩니다:
      ```
      scaled_value = (k - data_min) / (data_max - data_min)
      ```
    - 만약 `data_min == data_max`라면, 모든 값이 0.5로 설정된 리스트를 반환합니다.

    예제:
    --------
    1. 기본 사용법:
        >>> scale_data([10, 20, 30, 40, 50])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    
    2. 모든 값이 동일한 경우:
        >>> scale_data([5, 5, 5])
        [0.5, 0.5, 0.5]

    3. 정수와 실수가 섞인 경우:
        >>> scale_data([1.5, 2, 3, 4.5])
        [0.0, 0.16666666666666666, 0.5, 1.0]
    """
    data_min = min(data)  # 데이터의 최소값
    data_max = max(data)  # 데이터의 최대값

    # 모든 값이 동일한 경우 예외 처리
    if data_min == data_max:
        return [0.5] * len(data)

    # 데이터를 0과 1 사이로 스케일링
    scaled_data = []
    for k in data:
        scaled_value = (k - data_min) / (data_max - data_min)
        scaled_data.append(scaled_value)

    return sorted(scaled_data)