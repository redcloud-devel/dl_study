# Day 1: CNN 기본 - 합성곱 레이어
import torch
import torch.nn as nn

# 입력: (배치, 채널, 높이, 너비)
x = torch.randn(1, 1, 5, 5)

# 1채널 -> 2채널, 3x3 커널
conv = nn.Conv2d(1, 2, kernel_size=3, stride=1, padding=1)

y = conv(x)

print("x shape =", x.shape)
print("y shape =", y.shape)
