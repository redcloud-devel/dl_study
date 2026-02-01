# Day 5: 정규화(Regularization) - L2 (경사하강법에 적용)
import numpy as np

# 정규화: 가중치가 너무 커지는 것을 방지해 과적합 완화
# 데이터: y = 2x + 1
x = np.array([0, 1, 2, 3, 4], dtype=float)
y = 2 * x + 1

# 모델: y_hat = w*x + b
w = 0.0
b = 0.0
lr = 0.1
lam = 0.1  # L2 정규화 강도

for step in range(20):
    y_hat = w * x + b
    # MSE 기울기
    dw = np.mean(2 * (y_hat - y) * x)
    db = np.mean(2 * (y_hat - y))
    # L2 정규화 항 (bias는 보통 제외)
    dw += 2 * lam * w

    w -= lr * dw
    b -= lr * db

    if step % 5 == 0:
        mse = np.mean((y_hat - y) ** 2)
        reg = lam * (w ** 2)
        total = mse + reg
        print(f"step {step:02d}: w={w:.3f}, b={b:.3f}, mse={mse:.6f}, reg={reg:.6f}, total={total:.6f}")
