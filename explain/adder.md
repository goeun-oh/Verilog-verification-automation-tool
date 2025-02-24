# 📌 가산기 설계
---
## 🚀 주요 기능
  - adder.v: 1bit 덧셈 연산을 위한 gate 로직
  - adder_tb.v: 입력 txt 파일을 읽어와서 입력(a, b, cin), 출력(cout, sum)값 테스트
---

### ✅ 0. Full-Adder
![image](https://github.com/user-attachments/assets/7d655f46-7c9b-4b12-8a2e-0887b21b427e)
- 1 bit Full Adder
  
+ 입력을 a, b, cin, 출력을 cout, sum로 두는 로직
+ xor gate 2개, and gate 2개, or gate 1개로 이루어짐

  ![image](https://github.com/user-attachments/assets/b08636ae-9234-4328-8e3d-5c0ceb111eef)
- n bit full Adder

+ 1 bit Adder가 n개 이어진 구조
+ 직전 Adder의 cout이 다음 Adder에서 Cin 입력으로 들어감
+ 최종적으로, n bit a,b,sum과 1bit cout을 확인 가능 
  
### ✅ 1. adder 로직 설계 (adder.v)
📌 **기능 상세**

  - xor, and, or로 input, output, wire 연결
    1. input(a,b,cin), output(sum,cout), wire(s1,c1,c2) 선언
    2. 각 연결 및 연산부를 xor, and, or로 결합

### ✅ 2. adder_n 로직 설계 (adder_n.v)
📌 **기능 상세**

  - python(generate_vfile.py)에서 bit width를 입력 받고, n bit 가산기 모듈 adder_n.v 자동 생성
    1. adder.v n개를 연결
    

    
### ✅ 3. testbench 실행 (adder_tb.v)
📌 **기능 상세**
  - python(generate_tb.py)에서 bit width를 입력받고, adder_tb.v 자동 생성
    
  - file = $fopen("input_txt", "r")로 입력 txt 파일 read 후, 변수에 할당
    1. if (fd_in == 0) 이면 Error 메세지 출력 후 종료
    2. file이 존재한다면 다음 로직
   
  - $fscanf(file, "%d %d %d\n", a, b, cin)로 파일 한 줄씩 읽고 테스트 실행
    1. 각 연산당 1ns 실행
    2. 테스트 후, $display로 값 출력

  - $fwrite(fd_out, "%b %b %b -> sum: %b, cout: %b\n", a, b, cin, sum, cout)로 fd_out에 write
    1. verilog_output.txt 생성
    
  - $fclose(file)로 파일 닫기


