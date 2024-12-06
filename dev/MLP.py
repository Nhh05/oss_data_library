# 이 코드는 EsterHlav의 일부 아이디어와 구현을 참고하여 작성되었습니다.
# https://github.com/EsterHlav/MLP-Numpy-Implementation-Gradient-Descent-Backpropagation
# Copyright (c) 2017 EsterHlav
# Licensed under the MIT License.
# MIT License: https://opensource.org/licenses/MIT


import numpy as np

class MLPForMINIST:
    def __init__(self, input_length, hidden_length, output_length, learning_rate=0.01):
        self.input_length = input_length #필수 입력란
        self.hidden_length = hidden_length #필수 입력란
        self.output_length = output_length #필수 입력란
        self.learning_rate = learning_rate # 기본 : 0.01
        # W : 가중치
        # b : 편향
        # Z : 선형 변환 결과 (Z = X⋅W + b)
        # A : 활성화함수 통과후 sigmoid(Z)
        #w1 b1 은 입력층 -> 은닉층
        #w2 b2 은 은닉층 -> 출력층
        self.W1 = np.random.randn(input_length, hidden_length) * 0.01 #입력층 -> 은닉층 W
        self.b1 = np.zeros((1,hidden_length))
        self.W2 = np.random.randn(hidden_length, output_length) * 0.01 #은닉층 -> 출력층 W
        self.b2 = np.zeros((1,output_length))

    def sigmoid(self, x): #시그모이드 함수
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x): #시그모이드 도함수
        return x * (1 - x)
    
    def relu(self, x):
        return np.maximum(0, x)

    def relu_derivative(self, x):
        return np.where(x > 0, 1, 0)

    def softmax(self, x): #Softmax 함수 정의
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    
    #손실함수 MSE(X) -> Categorical Cross-Entropy
    def calc_loss(self, y, y_pred):
        m = y.shape[0]
        loss = -np.sum(y * np.log(y_pred + 1e-9)) / m
        return loss
    
    def forward(self,X): ## 순전파 - 단순계산
        self.Z1 = np.dot(X, self.W1) + self.b1
        self.A1 = self.sigmoid(self.Z1) #은닉층 출력값
        self.Z2 = np.dot(self.A1, self.W2) + self.b2
        self.A2 = self.softmax(self.Z2) # 출력층 출력값
        return self.A2

    def backward(self, X, y, y_pred): ##역전파 - 가중치조절
        m = X.shape[0]  # 배치 크기
        #은닉층 - 출력층에서의 기울기 계산
        dZ2 = y_pred-y #dz = y_hat - y
        dW2 = np.dot(self.A1.T, dZ2) / m 
        db2 = np.sum(dZ2, axis=0, keepdims=True) / m
        #
        dA1 = np.dot(dZ2, self.W2.T)
        dZ1 = dA1 * self.relu_derivative(self.A1)
        dW1 = np.dot(X.T, dZ1) / m
        db1 = np.sum(dZ1, axis=0, keepdims=True) / m
        #기울기 변경
        self.W1 -= self.learning_rate * dW1 
        self.b1 -= self.learning_rate * db1
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
    
    def fit(self, X_train, y_train, X_test, y_test, epoch=1000, patience=10):
        train_losses = []
        test_losses = []
        best_loss = float('inf')
        patient_count = 0
        for i in range(epoch):
            y_pred_train = self.forward(X_train)
            y_pred_test = self.forward(X_test)
            train_loss = self.calc_loss(y_train,y_pred_train)
            test_loss = self.calc_loss(y_test,y_pred_test)
            train_losses.append(train_loss)
            test_losses.append(test_loss)

            self.backward(X_train, y_train, y_pred_train)

            if i%100==0:
                print(f"epoch: {i} | train_loss: {train_loss} | test_loss: {test_loss}")
            if test_loss < best_loss:
                best_loss = test_loss
                patient_count = 0
            else:
                patient_count+=1
            if patient_count > patience:
                print(f"Early stopping at epoch{i}")
                break
        
        return train_losses, test_losses
    
    def predict(self, X):
        y_pred = self.forward(X)
        return np.argmax(y_pred, axis=1)

