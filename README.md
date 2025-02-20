### Verilog-verification-automation-tool
---
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
---
# Verilog-verification-automation-tool
## 📌 Develop Branch Guide

🚀 **이 브랜치는 개발 중인 코드가 포함된 `develop` 브랜치입니다.**
모든 새로운 기능(`feature/*`)은 이 브랜치에서 개발되며, 안정성이 확보된 후 `main` 브랜치로 병합됩니다.


## 📌 최신 변경 사항
📌 전체 변경 내역은 [CHANGELOG.md](CHANGELOG.md)에서 확인하세요.
