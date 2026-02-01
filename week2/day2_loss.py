# Day 2: 손실함수(MSE)의 의미
import numpy as np

# 손실함수: 예측과 정답의 차이를 수치로 표현
# predictions vs targets
pred = np.array([2.0, 3.0, 4.0, 5.0])
true = np.array([2.5, 2.7, 3.8, 5.2])

# MSE: 평균 제곱 오차(작을수록 좋음)
mse = np.mean((pred - true) ** 2)

print("pred =", pred)
print("true =", true)
print("MSE =", mse)
