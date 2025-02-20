# 📌 Verilog Verification Automation Tool

![GitHub repo size](https://img.shields.io/github/repo-size/goeun-oh/Verilog-verification-automation-tool)
![GitHub last commit](https://img.shields.io/github/last-commit/goeun-oh/Verilog-verification-automation-tool)
![GitHub contributors](https://img.shields.io/github/contributors/goeun-oh/Verilog-verification-automation-tool)

## 📖 프로젝트 소개
**Verilog Verification Automation Tool**은 Verilog로 설계된 8비트 가산기의 기능을 자동으로 검증하는 시스템입니다.  
Python을 활용하여 입력값을 생성하고, 시뮬레이션 결과를 자동 비교 및 검증합니다.

---

## 🔧 주요 기능
✅ **Verilog 자동 검증** - Python을 이용하여 Verilog 시뮬레이션을 자동화  
✅ **랜덤 입력값 생성** - 다양한 입력 조합을 자동 생성  
✅ **결과 비교 및 로그 저장** - 예측값과 시뮬레이션 결과를 비교하여 로그로 기록  
✅ **유닛 테스트 지원** - 다양한 테스트 케이스를 설정하여 검증  

---

## 🛠️ 기술 스택
- **HDL:** Verilog
- **Simulation:** ModelSim, Icarus Verilog
- **Programming:** Python
- **Communication:** File I/O, subprocess
- **Version Control:** Git & GitHub

---


## 🏗️ 팀원 역할 분담
### **🔹 1️⃣ Verilog 설계**
- **🛠️ 양지훈**: Verilog 설계 & 시뮬레이션 (`adder.v`, `adder_tb.v`)

### **🔹 2️⃣ Python 입력 생성**
- **💻 유승우**: Python 기반 입력 생성 (`generate_input.py`, `run_verilog.py`)

### **🔹 3️⃣ 결과 검증 & 오류 감지**
- **🔍 오고은**: Python 기반 결과 검증 및 오류 감지 (`verify_results.py`, `error_log.txt`)

