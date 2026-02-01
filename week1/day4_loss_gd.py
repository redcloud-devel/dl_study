# Day 4: 손실함수/경사하강법 개념 예제
import numpy as np

# 손실함수: 모델이 틀린 정도를 수치로 표현
# minimize f(x) = (x-3)^2

def f(x):
    return (x - 3.0)**2

def grad_f(x):
    return 2*(x - 3.0)

x = 10.0
lr = 0.1

# 경사하강법: 기울기 방향의 반대로 조금씩 이동해 최소값 찾기
for step in range(10):
    x = x - lr * grad_f(x)
    print(f"step {step:02d}: x={x:.4f}, f(x)={f(x):.6f}")
