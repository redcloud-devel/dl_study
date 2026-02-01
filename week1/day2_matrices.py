# Day 2: 행렬 연산의 핵심 개념 예제
import numpy as np

# 행렬: 벡터를 쌓아 만든 2차원 배열(선형 변환을 표현)
A = np.array([[1.0, 2.0], [3.0, 4.0]])
B = np.array([[2.0, 0.0], [1.0, 2.0]])

print("A =\n", A)
print("B =\n", B)
# 행렬 곱: 선형 변환의 합성
print("A @ B =\n", A @ B)
# 전치: 행과 열을 뒤집는 연산
print("A.T =\n", A.T)

# 역행렬: 변환을 되돌리는 행렬(존재할 때만 가능)
A_inv = np.linalg.inv(A)
print("A_inv =\n", A_inv)
print("A @ A_inv =\n", A @ A_inv) # 단위행렬
