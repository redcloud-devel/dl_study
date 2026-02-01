# Day 1: 지도학습 기본 (선형회귀)
import numpy as np

# 지도학습: (입력 x, 정답 y) 쌍으로 규칙을 학습
# toy data: y = 2x + 1 + noise
x = np.array([0, 1, 2, 3, 4], dtype=float)
y = 2 * x + 1 + np.array([0.2, -0.1, 0.1, -0.2, 0.0])
# random noise 
# noise = np.random.normal(0, 0.1, size=x.shape)
# y = 2 * x + 1 + noise

# 선형회귀: y = w*x + b 형태로 데이터에 맞춤
# 닫힌해(최소제곱): theta = (X^T X)^{-1} X^T y
X = np.vstack([x, np.ones_like(x)]).T  # [x, 1]
theta = np.linalg.inv(X.T @ X) @ X.T @ y

print("theta (slope, intercept) =", theta)
print("pred for x=5 =", theta[0]*5 + theta[1])

# 실제값 vs 예측값 차이(잔차)
y_pred = X @ theta
residuals = y - y_pred
print("y =", y)
print("y_pred =", y_pred)
print("residuals (y - y_pred) =", residuals)
