# Day 2: CNN 기본 - 풀링
import torch
import torch.nn as nn

x = torch.randn(1, 1, 4, 4)

pool = nn.MaxPool2d(kernel_size=2, stride=2)

y = pool(x)

print("x =\n", x)
print("y =\n", y)
print("x shape =", x.shape)
print("y shape =", y.shape)
