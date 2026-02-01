# Day 5: 역전파(해석적 기울기)와 비교
import numpy as np

# y = w*x + b, loss = (y_pred - y_true)^2
x = 3.0
y_true = 7.0

w = 1.0
b = 0.0

# 해석적 기울기: 수식으로 직접 미분
# y_pred = w*x + b
# dL/dw = 2*(y_pred - y_true)*x
# dL/db = 2*(y_pred - y_true)

y_pred = w * x + b

dw = 2 * (y_pred - y_true) * x
db = 2 * (y_pred - y_true)

print("y_pred =", y_pred)
print("dw =", dw)
print("db =", db)
