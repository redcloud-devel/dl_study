# Day 5: 모델 저장/불러오기
import torch
import torch.nn as nn

# state_dict: 모델 파라미터만 저장/복원하는 표준 방식
model = nn.Linear(1, 1)

# 저장
path = "week4_linear.pt"
torch.save(model.state_dict(), path)

# 로드
model2 = nn.Linear(1, 1)
model2.load_state_dict(torch.load(path))
model2.eval()

print("loaded ok")
