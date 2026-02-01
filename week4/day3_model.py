# Day 3: PyTorch 모델 정의
import torch
import torch.nn as nn

# nn.Module: 파이토치 모델의 기본 클래스
# 선형 회귀 모델, 랜덤한 W, b 로 들어감
model = nn.Linear(1, 1)

# 임의 입력
x = torch.tensor([[1.0], [2.0], [3.0]])

y_pred = model(x)
print("y_pred =", y_pred.detach().squeeze().tolist())
