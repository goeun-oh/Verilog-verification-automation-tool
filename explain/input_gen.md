# generate_input.py
---
## 🚀 주요 기능
  - generate_input.py	: 랜덤 8비트 입력값(A, B, Cin) 생성 및 저장 (input.txt)

### ✅ 1. Python으로 입력 데이터 생성(generate_input.py)

📌 **코드 설명**

  - with open("대상파일", "w"(쓰기) or "r"(읽기)) as file
    1. file을 open하고 close()안하는 것을 방지하기 위해 사용
    2. open 구문 종료시 close()가 동작
    3. random.randint(0,1)로 생성된 값 txt 파일에 저장하기 위해 사용
