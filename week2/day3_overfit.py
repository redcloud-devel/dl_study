# Day 3: 과적합 직관 (다항식 피팅)
import numpy as np
import matplotlib.pyplot as plt

# 과적합: 훈련 데이터에 과도하게 맞춰 일반화가 안 되는 현상
# small dataset
x = np.array([-2, -1, 0, 1, 2], dtype=float)
y = np.array([4.1, 1.0, 0.2, 1.1, 3.9])

# 낮은 차수 vs 높은 차수 비교
# polyfit: 주어진 (x,y)에 대해 deg차 다항식 계수를 최소제곱으로 구함
#   예) deg=2 -> ax^2 + bx + c 의 [a, b, c] 반환
coef_deg2 = np.polyfit(x, y, deg=2)
coef_deg4 = np.polyfit(x, y, deg=4)

print("deg=2 coefficients =", coef_deg2)
print("deg=4 coefficients =", coef_deg4)

# polyval: 계수와 x를 넣어 다항식 값(예측값)을 계산
# 훈련 데이터에서 오차 비교
p2 = np.polyval(coef_deg2, x)
p4 = np.polyval(coef_deg4, x)

print("deg=2 train MSE =", np.mean((p2 - y) ** 2))
print("deg=4 train MSE =", np.mean((p4 - y) ** 2))

# 시각화: 훈련 데이터와 두 모델 곡선 비교
x_line = np.linspace(-2.5, 2.5, 200)
y_line_deg2 = np.polyval(coef_deg2, x_line)
y_line_deg4 = np.polyval(coef_deg4, x_line)

plt.figure()
plt.scatter(x, y, label="data", color="black")
plt.plot(x_line, y_line_deg2, label="deg=2 fit")
plt.plot(x_line, y_line_deg4, label="deg=4 fit")
plt.title("Polynomial Fit: Underfit vs Overfit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
