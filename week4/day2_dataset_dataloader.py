# Day 2: Dataset/Dataloader 기본
import torch
from torch.utils.data import TensorDataset, DataLoader

# Dataset: (x, y) 묶음을 저장
# DataLoader: 배치 단위로 섞어서 공급
x = torch.arange(0, 10, dtype=torch.float32).unsqueeze(1)
y = 2 * x + 1

dataset = TensorDataset(x, y)
loader = DataLoader(dataset, batch_size=4, shuffle=True)

for xb, yb in loader:
    print("batch x:", xb.squeeze().tolist(), "batch y:", yb.squeeze().tolist())
