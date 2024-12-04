MNIST 데이터셋을 학습시킬 때, 원핫인코딩(One-Hot Encoding)은 레이블(정답 값)을 모델이 이해할 수 있는 형식으로 변환하기 위해 사용됨


원핫인코딩이 사용되는 이유

문제점 1: 정수형 레이블은 "순서"를 암시
정수형 레이블(5)은 모델이 5 > 4 또는 5와 4의 거리가 1이라는 순서 또는 관계를 가정하게 할 수 있습니다.
그러나 MNIST 레이블은 이러한 순서나 거리 개념이 없습니다. (예: 5와 4는 전혀 관련 없는 독립적인 숫자)

문제점 2: 손실 함수에서 부적합
분류 문제에서는 Categorical Cross-Entropy 또는 Sparse Categorical Cross-Entropy 같은 손실 함수를 사용하는데, 정수형 레이블은 Sparse Categorical Cross-Entropy에서만 적합합니다.
원핫인코딩을 사용하면 Categorical Cross-Entropy 손실 함수를 사용할 수 있고, 이는 모델이 확률 출력을 학습하도록 유도합니다.