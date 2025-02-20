# 📌 Verilog-verification-automation-tool
---
## 🚀 주요 기능
  - generate_input.py	: 랜덤 8비트 입력값(A, B, Cin) 생성 및 저장 (input.txt)
  - run_verilog.py : Verilog 시뮬레이터 실행 자동화 (verilog & pyverilog)
---
### ✅ 1. Python으로 입력 데이터 생성(generate_input.py)

📌 **기능 상세**

  - with open("대상파일", "w"(쓰기) or "r"(읽기)) as file
    1. file을 open하고 close()안하는 것을 방지하기 위해 사용
    2. open 구문 종료시 close()가 동작
    3. random.randint(0,1)로 생성된 값 txt 파일에 저장하기 위해 사용
    
### ✅ 2. Python으로 Verilog 시뮬레이션 실행(run_verilog.py)

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


