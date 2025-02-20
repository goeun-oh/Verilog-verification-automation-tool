### Verilog-verification-automation-tool
---
1. 전체 구조 (파일 간 관계)
  - generate_input.py	: 랜덤 8비트 입력값(A, B, Cin) 생성 및 저장 (input.txt)
  - run_verilog.py : Verilog 시뮬레이터 실행 자동화 (verilog & pyverilog)
---
2. Python으로 입력 데이터 생성(generate_input.py)
  - Pyverilog 기능
  - (1) code parser
  - (2) dataflow analyzer
  - (3) control-flow analyzer
  - (4) code generator
  - 
  - VerilogDataflowAnalyzer로 code generator 기능을 사용
  - 실행 결과를 verilog_output.txt로 저장
  - verilog_output.txt와 실제 verilog 결과 값과 비교로 검증
