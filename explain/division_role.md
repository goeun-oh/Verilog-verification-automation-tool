
### **🔹 1️⃣ Verilog 설계**
**🛠️ 양지훈**: 
- Verilog를 기반으로 Full Adder 설계 & 시뮬레이션 (`adder.v`)
- input.txt 의 data를 input으로 하고, 도출된 output을 `verilog_output.txt`에 기록하는 testbench 작성 ( `adder_tb.v`) 
- Python output과 Verilog ouptut을 비교한 후 일치 여부를 csv 파일 형식으로 기록하는 Python 파일 작성 (`txt_to_csv.py`) <br>
**[가산기 설계](https://github.com/goeun-oh/Verilog-verification-automation-tool/blob/hotfix_v01/explain/adder.md)**
<br>

### **🔹 2️⃣ Python 입력 생성**
**💻 유승우**: 
- random input을 생성하여 `input.txt`에 기록하는 Python 프로그램 작성 (`generate_input.py`)
- Python output과 Verilog ouptut을 비교한 후 일치 여부를 csv 파일 형식으로 기록하는 Python 파일 작성 (`txt_to_csv.py`) <br>
**[Random Input 생성 txt_to_csv 설명](https://github.com/goeun-oh/Verilog-verification-automation-tool/blob/hotfix_v01/explain/gen_input.md)**
<br>

### **🔹 3️⃣ 결과 검증 & 오류 감지**
**🔍 오고은**:
- **프로젝트 총괄**
- Python 기반 결과 도출 및 Verilog Output과 비교 (`run_python_adder.py`, `compare_files.py`)
- Git Action을 활용한 자동화 스크립트 작성 (`github/workflows/verilog_verification.yml`) <br>
**[Python vs Verilog 결과 비교](https://github.com/goeun-oh/Verilog-verification-automation-tool/blob/hotfix_v01/explain/comparison.md)**
<br>

### **🔹 4️⃣ 검증 자동화 연구 & 기획**
**🚀 유진모**:  
- 프로젝트 기획 및 아이디어 구체화
- 문서 구조 및 개발 방향성 제안
- Verilog & Python 기반의 검증 자동화 논문 조사
<br>
