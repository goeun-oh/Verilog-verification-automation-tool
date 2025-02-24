# 📌 1 Bit 가산기 설계
---
## 🚀 주요 기능
  - adder.v: 1bit 덧셈 연산을 위한 gate 로직
---

### ✅ 0. 1 Bit Full-Adder
![image](https://github.com/user-attachments/assets/7d655f46-7c9b-4b12-8a2e-0887b21b427e)
- **1 bit Full Adder**
  
  1. 입력을 a, b, cin, 출력을 cout, sum로 두는 로직
  2. xor gate 2개, and gate 2개, or gate 1개로 이루어짐

  
### ✅ 1. adder 로직 설계 (adder.v)
📌 **기능 상세**

  - xor, and, or로 input, output, wire 연결
    1. input(a,b,cin), output(sum,cout), wire(s1,c1,c2) 선언
    2. 각 연결 및 연산부를 xor, and, or로 결합



