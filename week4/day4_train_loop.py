# Day 4: 학습 루프 기본
import torch
import torch.nn as nn

# 데이터
x = torch.arange(0, 10, dtype=torch.float32).unsqueeze(1)
y = 2 * x + 1

# 모델/손실/옵티마이저
model = nn.Linear(1, 1)
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(20):
    # 1) 기울기 초기화
    optimizer.zero_grad()
    # 2) 순전파
    y_pred = model(x)
    # 3) 손실 계산
    loss = criterion(y_pred, y)
    # 4) 역전파
    loss.backward()
    # 5) 파라미터 업데이트
    optimizer.step()
    if epoch % 5 == 0:
        print(f"epoch {epoch:02d} loss={loss.item():.6f}")
