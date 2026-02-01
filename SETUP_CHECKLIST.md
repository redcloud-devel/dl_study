# 환경 세팅 체크리스트

## 1) 필수 도구
- [x] macOS 업데이트 확인
- [x] 터미널 기본 쉘 확인 (zsh)
- [x] Git 설치 확인 (`git --version`)

## 2) 파이썬 환경
- [x] Python 3.10+ 설치 확인 (`python3 --version`)
- [x] 가상환경 도구 선택
  - [x] venv 또는
  - [ ] conda
- [x] 프로젝트용 가상환경 생성
- [x] 가상환경 활성화 확인

## 3) 패키지 설치 (예시)
- [x] pip 최신화 (`python -m pip install --upgrade pip`)
- [x] 핵심 라이브러리 설치
  - [x] numpy
  - [x] matplotlib
  - [x] pandas
  - [x] scikit-learn
  - [x] torch
  - [x] torchvision
  - [x] notebook 또는 jupyterlab

## 4) 개발 환경
- [x] VS Code 설치
- [x] Python 확장 설치
- [ ] Jupyter 확장 설치
- [x] 터미널에서 `code` 명령 확인

## 5) 실행 확인
- [ ] 파이썬 REPL에서 import 테스트
- [ ] Jupyter 실행 확인
- [ ] 간단한 텐서 연산 실행

## 6) 선택 사항
- [ ] GPU 사용 계획 확인
- [ ] MPS(Apple Silicon) 지원 확인
- [ ] 데이터/노트 폴더 구조 정리
