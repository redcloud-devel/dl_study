# Day 2: MLP(다층 퍼셉트론) 순전파
import numpy as np

# 입력 (3차원)
x = np.array([1.0, 0.5, -1.0])

# 1층 가중치(3->2), 바이어스(2)
W1 = np.array([[0.2, -0.5, 0.1],
               [0.7,  0.3, -0.2]])
b1 = np.array([0.1, -0.1])

# 2층 가중치(2->1), 바이어스(1)
W2 = np.array([[0.6, -0.4]])
b2 = np.array([0.05])

# 활성화 함수: ReLU (음수는 0)
relu = lambda t: np.maximum(0, t)

# 순전파: 1층 -> 활성화 -> 2층
h = relu(W1 @ x + b1)
y = W2 @ h + b2

print("x =", x)
print("h =", h)
print("y =", y)
