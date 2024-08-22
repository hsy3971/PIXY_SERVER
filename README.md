# PIXY
<img src="https://github.com/user-attachments/assets/a1b4f8ce-1b2f-4d03-a9c7-a0f8a47dc731" alt="image"></img>
## 개요
무인매장 맞춤형 AI PIXY로써 리테일 기업을 비롯한 다양한 무인매장의 점주들에게 제공하는 AI 서비스입니다.

다음과 같은 기능을 제공합니다.
- 맞춤형 고객 응대: 랭체인과 ChatGPT를 활용하여 매장별 맞춤형 챗봇을 통해 고객 응대를 지원합니다.
- CCTV 모니터링: YOLOv8를 이용해 사람을 감지하고, LSTM 기반 자세 추정을 통해 절도와 화재를 감지합니다.
- 재고 관리: 머신러닝을 활용한 판매량 예측으로 효율적인 재고 관리를 제공합니다.

## 기능별 페이지
### 이상행동 탐지
<img src="https://github.com/user-attachments/assets/11ab02d5-2147-4c81-af3b-46e8c6436115" alt="image"></img>

### 화재 탐지
<img src="https://github.com/user-attachments/assets/7691510d-1e8e-4f1d-9e74-510460825bef" alt="image"></img>

### 판매예측
<img src="https://github.com/user-attachments/assets/2283a698-8387-4c47-9e23-a99f58d1754c" alt="image"></img>

## RAG-LLM
<img src="https://github.com/user-attachments/assets/0da857b8-ad42-4605-8859-d0cb426203e7" alt="image"></img>

## 프로젝트 구조
- `/frontend`: React 기반 사용자 인터페이스
- `/backend`: Django REST Framework 기반 API 서버
- `/custom-llm`: BERT 기반 커스텀 언어 모델
- `/ai-models`: 머신러닝 및 딥러닝 모델
  - `/sales-prediction`: RandomForest 기반 시계열 데이터 예측 모델
  - `/anomaly-detection`: Isolation Forest 기반 이상 행동 예측 모델
  - `/fire-prediction`: XGBoost 기반 화재 예측 모델

## 주요 기능
- 대시보드를 통한 실시간 데이터 시각화 및 분석
- RESTful API를 통한 효율적인 데이터 처리 및 모델 결과 제공
- 자연어 처리 기반의 사용자 쿼리 해석 및 응답 생성
- 시계열 데이터를 활용한 미래 트렌드 예측
- 실시간 이상 행동 감지 및 즉각적인 알림 시스템
- 다양한 요인을 고려한 정확한 화재 위험 예측 및 조기 경보 시스템

## 기술 스택
- 프론트엔드: React, Redux, Material-UI
- 백엔드: Django, Django REST Framework
- 데이터베이스: Mysql, Redis
- AI/ML: TensorFlow, PyTorch, Scikit-learn, RandomForest
- 인프라: AWS EC2, S3, RDS

## 서비스 플로우
<img src="https://github.com/user-attachments/assets/b6ffe3ef-7259-4149-8df0-bdf522ee846e" alt="image"></img>

## 아키텍처 정의서
<img src="https://github.com/user-attachments/assets/dd538b71-d17b-4697-ac54-a5bba98f40e7" alt="image"></img>

## ERD
<img src="https://github.com/user-attachments/assets/26d32591-86ae-4059-92ea-e1ebbf235e9c" alt="image"></img>

## AI 적용기술
### 이상행동 탐지 모델

<img src="https://github.com/user-attachments/assets/50f7c260-73c8-4132-8ce5-2ad9e83e5a9b" alt="image"></img>

### 화재탐지 모델

<img src="https://github.com/user-attachments/assets/42ea6a6a-d8c4-44fa-9acd-f4d1d8676c08" alt="image"></img>

### 판매예측 모델

<img src="https://github.com/user-attachments/assets/de59e5aa-c4ab-42a1-b269-36b6f4a3650b" alt="image"></img>

### RAG-LLM

<img src="https://github.com/user-attachments/assets/c2bfa631-ed88-43bb-bb72-4c1689ca5c99" alt="image"></img>
