# 모듈 교차 검증 - `Python vs Verilog 결과 비교`

## 📖 result_verification
verilog simulation 결과를 교차 검증하기위해 
Python 상에서 `adder.v`와 같은 기능을 하는 가산기를 구현하고, 이 결과를 verilog simulation 결과와 일치하는지 확인합니다.


## 🚀 주요 기능

### ✅ 1. Python에서 Full Adder 연산 수행 (`run_python_adder.py`)
이 스크립트는 **Python에서 Full Adder 연산을 수행**하고, 결과를 `python_output.txt`에 저장합니다.  

📌 **기능 상세**
- `input.txt` 파일에서 Full Adder 테스트 데이터를 읽습니다.
- Python 논리 연산을 통해 `sum`, `cout`을 계산합니다.
- 결과를 `python_output.txt`에 저장합니다.

### ✅ 2. Python과 Verilog의 결과 비교 (`compare_files.py`)
이 스크립트는 python_output.txt와 verilog_output.txt를 비교하여 불일치 여부를 검사합니다.
Python과 Verilog의 실행 결과가 다른 경우 불일치 내용을 출력합니다.  

📌 **기능 상세**
- `python_output.tx`t와 `verilog_output.txt`의 내용을 한 줄씩 비교합니다.
- 모든 줄이 일치하면 "결과가 완벽하게 일치합니다!" 메시지를 출력합니다
