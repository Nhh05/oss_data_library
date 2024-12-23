## oss_png_transfer 라이브러리

`oss_png_transfer` : MINIST 데이터셋을 기반으로 PNG 파일 읽기(only grayscale), 데이터 전처리, 간단한 MLP 모델 학습을 해볼 수 있는 Python 라이브러리 입니다.

### 기능
1. **PNGProcessor.py**:
   - PNG 파일의 데이터 여는 기능.
   - 흑백(그레이스케일) 이미지 색상 반전.
   - (JPG는 추후 업데이트 예정)

2. **DataPreProcessor.py**:
    - 데이터 섞기, train, test 데이터 분리
        - 섞는 과정에서 시드 값(seed = 42)를 설정하면 동일한 결과를 낼 수 있습니다.
        - 기본 train, test 분할 비율은 7:3 이고, 개별 정의 가능합니다.

    - OneHot 인코딩
        - 숫자형 라벨(예: 0, 1, 2)을 One-hot 벡터 형식으로 변환한다.
        - ex) [0, 1, 2] → [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        
    - 데이터 정규화
        - 데이터 최소값과 최댓값 기준으로 0~1범위로 정규화한다.
        - 모든 값이 동일할 경우, 예외처리로 모든 데이터가 0.5로 설정된다.

3. **MLPForMINIST.py**:
   - 입력층, 은닉층, 출력층의 노드 개수 설정.
   - 은닉층은 한겹으로 고정
   - 반복횟수(epoch = 1000), 학습률(learning_rate = 0.1) 설정가능
   - 모델 파라미터 저장/불러오기 지원.
   -> 학습시킨 이후 모델을 저장하고, 파라미터를 불러와서 model.forward()로 이미지 예측할 수 있음

## 설치
```bash
pip install oss-png-transfer
