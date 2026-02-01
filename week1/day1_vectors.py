# Day 1: 벡터/내적/노름의 핵심 개념 예제
import numpy as np

# 벡터: 숫자의 리스트(특징들의 모음)
v = np.array([1.0, 2.0, 3.0])
w = np.array([4.0, 5.0, 6.0])

print("v =", v)
print("w =", w)
# 내적: 두 벡터의 방향 유사도(같은 방향이면 큼, 직교면 0)
print("dot(v, w) =", np.dot(v, w))
# L2 노름: 벡터의 길이
print("L2 norm of v =", np.linalg.norm(v)) # linear algebra

# 코사인 유사도: 방향만 비교하는 유사도(-1~1)
cos_sim = np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w)) 
print("cosine similarity =", cos_sim)
