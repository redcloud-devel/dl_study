# Day 3: 미분/연쇄법칙 개념 예제(수치 미분으로 확인)
import numpy as np

# 함수와 미분: 기울기(변화율)를 계산
# f(x) = x^2 + 3x + 1
# f'(x) = 2x + 3

def f(x):
    return x**2 + 3*x + 1

def f_prime(x):
    return 2*x + 3

x = 2.0
h = 1e-5
# 수치 미분: 아주 작은 변화량으로 기울기 근사
num_grad = (f(x + h) - f(x - h)) / (2*h)

print("f(x) =", f(x))
print("analytic grad =", f_prime(x))
print("numeric grad =", num_grad)

# 연쇄법칙: 합성함수 미분 (g(x) = (3x + 1)^2)
# g'(x) = 2*(3x+1)*3

def g(x):
    return (3*x + 1)**2

def g_prime(x):
    return 2*(3*x + 1)*3

print("g'(x) =", g_prime(x))
num_grad_g = (g(x + h) - g(x - h)) / (2*h)
print("numeric grad =", num_grad_g)