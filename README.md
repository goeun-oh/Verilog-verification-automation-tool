# 📌 Verilog Verification Automation Tool

![GitHub repo size](https://img.shields.io/github/repo-size/goeun-oh/Verilog-verification-automation-tool)
![GitHub last commit](https://img.shields.io/github/last-commit/goeun-oh/Verilog-verification-automation-tool)
![GitHub contributors](https://img.shields.io/github/contributors/goeun-oh/Verilog-verification-automation-tool)

## 📖 프로젝트 소개
이 프로젝트는 **Verilog 연산 결과를 자동으로 검증하는 Python 기반의 도구**입니다.  
Python에서 Full Adder 연산을 수행한 결과와 Verilog 시뮬레이션 결과를 비교하여 검증하는 자동화 시스템을 구현하였습니다.
<br>

## 🔧 주요 기능
✅ **Verilog 자동 검증** - Python을 이용하여 Verilog 시뮬레이션을 자동화  
✅ **랜덤 입력값 생성** - 다양한 입력 조합을 자동 생성  
✅ **결과 비교 및 로그 저장** - 예측값과 시뮬레이션 결과를 비교하여 로그로 기록  
✅ **유닛 테스트 지원** - 다양한 테스트 케이스를 설정하여 검증  
<br>


## 🏗️ 팀원 역할 분담
### **🔹 1️⃣ Verilog 설계**
**🛠️ 양지훈**: 
- Verilog를 기반으로 Full Adder 설계 & 시뮬레이션 (`adder.v`)
- input.txt 의 data를 input으로 하고, 도출된 output을 `verilog_output.txt`에 기록하는 testbench 작성 ( `adder_tb.v`)

### **🔹 2️⃣ Python 입력 생성**
**💻 유승우**: 
- random input을 생성하여 `input.txt`에 기록하는 Python 프로그램 작성 (`generate_input.py`)
- Python output과 Verilog ouptut을 비교한 후 일치 여부를 csv 파일 형식으로 기록하는 Python 파일 작성 (`txt_to_csv.py`)

### **🔹 3️⃣ 결과 검증 & 오류 감지**
**🔍 오고은**:
- **프로젝트 총괄**
- Python 기반 결과 도출 및 Verilog Output과 비교 (`run_python_adder.py`, `compare_files.py`)
- Git Action을 활용한 자동화 스크립트 작성 (`github/workflows/verilog_verification.yml`)

### **🔹 4️⃣ 테스트 자동화 및 프로젝트 최적화**
- **🚀 유진모**:  
<br>


# 📂 파일 구조 (feature/result_verification)
📦 Verilog-verification-automation-tool <br>
 ┣ 📜 `README.md`                 # 전체 프로젝트 설명 파일

 🔹 Verilog 코드 <br>
 ┣ 📜 `adder.v`                   # Verilog Full Adder 코드 <br>
 ┣ 📜 `adder_tb.v`                # Verilog Testbench <br>
 ┣ 📜 `verilog_output.txt`        # Verilog 실행 결과 저장

🔹 입력 데이터 생성 <br>
 ┣ 📜 `generate_input.py`         # random input을 생성하여 input.txt 에 저장 <br>
 ┣ 📜 `input.txt`                 # Full Adder 테스트 입력값


🔹 Python 연산 및 결과 저장 <br>
 ┣ 📜 `run_python_adder.py`      # Python에서 Full Adder 실행 및 결과 저장 <br>
 ┣ 📜 `python_output.txt`         # Python 연산 결과 저장

🔹 결과 비교 및 검증 <br>
 ┣ 📜 `compare_files.py`          # Python과 Verilog 결과 비교 스크립트 <br>
 ┣ 📜 `txt_to_csv.py`             # compare_files.py의 결과를 csv 형식으로 저장 
<br>

# 📌 프로젝트 변경 기록
🔹 최신 변경 사항은 아래에서 확인하세요!  
📌 **[CHANGELOG.md (develop branch)](https://github.com/goeun-oh/Verilog-verification-automation-tool/blob/develop/CHANGELOG.md)**

