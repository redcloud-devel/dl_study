# Day 4: 경사하강법으로 선형회귀 학습
import numpy as np

# 데이터: y = 2x + 1
x = np.array([0, 1, 2, 3, 4], dtype=float)
y = 2 * x + 1

# 모델: y_hat = w*x + b (학습할 파라미터 w, b)
w = 0.0
b = 0.0
lr = 0.1

for step in range(20):
    y_hat = w * x + b
    # MSE의 기울기(미분)로 파라미터 업데이트
    dw = np.mean(2 * (y_hat - y) * x)
    db = np.mean(2 * (y_hat - y))
    w -= lr * dw
    b -= lr * db
    if step % 5 == 0:
        loss = np.mean((y_hat - y) ** 2)
        print(f"step {step:02d}: w={w:.3f}, b={b:.3f}, loss={loss:.6f}")
