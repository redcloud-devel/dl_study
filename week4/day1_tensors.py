# Day 1: PyTorch 텐서 기본
import torch

# 텐서: 파이토치의 기본 데이터 구조(NumPy 배열과 유사)
# 텐서 생성
x = torch.tensor([1.0, 2.0, 3.0])
A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

print("x =", x)
print("A =\n", A)
print("A @ A =\n", A @ A)

# 자동 미분: requires_grad=True로 기울기 추적
x = torch.tensor(3.0, requires_grad=True)
y = x**2 + 3*x + 1

y.backward()
print("dy/dx =", x.grad)
