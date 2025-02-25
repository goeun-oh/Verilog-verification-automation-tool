# 📌 N Bit 가산기 설계
---
## 🚀 주요 기능
  - adder_n.v: n bit 덧셈 연산을 위한 로직
---

### ✅ 0. N Bit Full-Adder
  ![image](https://github.com/user-attachments/assets/b08636ae-9234-4328-8e3d-5c0ceb111eef)

  - 1 bit Adder가 n개 이어진 구조
  - 직전 Adder의 cout이 다음 Adder에서 Cin 입력으로 들어감
  - 최종적으로, n bit a,b,sum과 1bit cout을 확인 가능

### ✅ 1. adder_n 로직 설계 (adder_n.v)
📌 **기능 상세**

  - python(generate_vfile.py)에서 bit width를 입력 받고, n bit 가산기 모듈 adder_n.v 자동 생성
    1. adder.v n개를 연결
    
