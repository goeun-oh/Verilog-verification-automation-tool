# 📌 Verilog-verification-automation-tool
---
## 🚀 주요 기능
  - adder.v: 1bit 덧셈 연산을 위한 gate 로직
  - adder_tb.v: 입력 txt 파일을 읽어와서 입력(a, b, cin), 출력(cout, sum)값 테스트
---

### ✅ 0. Full-Adder
![image](https://github.com/user-attachments/assets/7d655f46-7c9b-4b12-8a2e-0887b21b427e)

+ 입력을 a, b, cin, 출력을 cout, sum로 두는 로직
+ xor gate 2개, and gate 2개, or gate 1개로 이루어짐
  
### ✅ 1. adder 로직 설계 (adder.v)
📌 **기능 상세**

  - xor, and, or로 input, output, wire 연결
    1. input(a,b,cin), output(sum,cout), wire(s1,c1,c2) 선언
    2. 각 연결 및 연산부를 xor, and, or로 결합

    
### ✅ 2. testbench 실행 (adder_tb.v)
📌 **기능 상세**
    
  - file = $fopen(input_file, "r")로 입력 txt 파일 read 후, 변수에 할당
    1. if (file == 0) 이면 Error 메세지 출력 후 종료
    2. file이 존재한다면 다음 로직
   
  - $fscanf(file, "%d %d %d\n", a, b, cin)로 파일 한 줄씩 읽고 테스트 실행
    1. 각 연산당 1ns 실행
    2. 테스트 후, $display로 값 출력

    
  - $fclose(file)로 파일 닫기


### ✅ 3. 결과 출력 및 파형
![image](https://github.com/user-attachments/assets/84aff1b9-7caa-41a3-9b9a-cc85e9b62587)
+ 입력(a,b,cin)과 출력(sum,cout) 값에 따른 출력 결과


![image](https://github.com/user-attachments/assets/e523e145-1cfa-4962-9958-1eff2b88a430)
+ 입력 a=1, b=0, cin=0 / 출력 cout=0, sum=1의 파형
