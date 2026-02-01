# Day 5: 함수와 기울기(접선) 시각화
import numpy as np
import matplotlib.pyplot as plt

# 함수 그래프: 곡선의 모양과 값의 변화를 확인
# f(x) = x^2
x = np.linspace(-3, 3, 200)
y = x**2

plt.figure()
plt.plot(x, y, label="f(x)=x^2")

# 특정 지점 x0에서의 접선(기울기)
x0 = 1.0
slope = 2*x0

tangent = slope * (x - x0) + x0**2
plt.plot(x, tangent, "--", label="tangent at x=1")

plt.legend()
plt.title("Function and tangent")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
