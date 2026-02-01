# Day 3: 활성화 함수 비교
import numpy as np

# 활성화 함수: 비선형성을 추가해 표현력을 높임
x = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])

# sigmoid: (0,1)로 압축
sigmoid = lambda t: 1 / (1 + np.exp(-t))
# tanh: (-1,1)로 압축
tanh = lambda t: np.tanh(t)
# ReLU: 음수는 0, 양수는 그대로
relu = lambda t: np.maximum(0, t)

print("x =", x)
print("sigmoid =", sigmoid(x))
print("tanh =", tanh(x))
print("relu =", relu(x))
