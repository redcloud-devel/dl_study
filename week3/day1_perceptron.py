# Day 1: 퍼셉트론(단일 뉴런) 기본
import numpy as np

# 퍼셉트론: 입력의 가중합에 활성화(계단함수)를 적용
# 입력(2차원)과 가중치, 바이어스
x = np.array([1.0, 0.5])
w = np.array([0.8, -0.3])
b = 0.1

# 가중합 z = w·x + b
z = np.dot(x, w) + b

# 계단 함수(퍼셉트론 활성화)
# z > 0 이면 1, 아니면 0
out = 1 if z > 0 else 0

print("x =", x)
print("w =", w)
print("b =", b)
print("z =", z)
print("out =", out)
