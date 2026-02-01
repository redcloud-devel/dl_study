# Day 5: MNIST 데이터 로드 미리보기
import torch
from torchvision import datasets, transforms

transform = transforms.ToTensor()
train_ds = datasets.MNIST(root="./data", train=True, download=True, transform=transform)

x, y = train_ds[0]
print("x shape =", x.shape, "label=", y)
