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

  - Pyverilog 사용
  
  - Pyverilog 기능
    1. code parser
    2. dataflow analyzer
    3. control-flow analyzer
    4. code generator
    
  - Pyverilog의 기능 중 VerilogDataflowAnalyzer로 code generator 기능을 사용
    1. 실행 결과를 verilog_output.txt로 저장
    2. verilog_output.txt와 실제 verilog 결과 값과 비교로 검증

  - analyzer = VerilogDataflowAnalyzer(verilog_file, noreorder=True, topmodule='adder')
analyzer.generate()
    1. topmodule='adder'를 지정하여 "adder"라는 이름의 최상위 모듈을 분석 대상으로 설정
    2. analyzer.generate()를 호출하여 데이터 흐름 분석을 수행
    3. noreorder=True 일반적으로 최적화를 위해 내부적으로 연산 순서를 변경하지 않고 순서를 그대로 유지한 채로 분석
