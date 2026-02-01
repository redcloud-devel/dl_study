# Day 4: 역전파 직관 (수치 미분으로 확인)
import numpy as np

# 간단한 1층 모델: y = w*x + b
x = 3.0
y_true = 7.0

w = 1.0
b = 0.0

# 손실: MSE

def loss(w, b):
    y_pred = w * x + b
    return (y_pred - y_true) ** 2

# 수치 미분: 작은 변화량으로 기울기 근사
h = 1e-5

dw = (loss(w + h, b) - loss(w - h, b)) / (2*h)
db = (loss(w, b + h) - loss(w, b - h)) / (2*h)

print("loss =", loss(w, b))
print("numeric dw =", dw)
print("numeric db =", db)
