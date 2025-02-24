# 🚀 Verilog Verification Automation(verilog_verification.yml)

## 📌 개요
- GitHub Actions를 활용하여 **Verilog 검증 자동화** 수행
- **매 1분마다 실행되는 CI/CD** 설정 (cron 스케줄링 적용)
- Verilog 시뮬레이션 및 Python 검증 로직 자동 실행
- GitHub에 자동으로 결과 파일 업데이트 및 비교 수행

## 🔄 주요 기능
- **자동 실행**: GitHub Actions를 통해 **Verilog 및 Python 코드 실행 자동화**
- **Verilog 및 Python 입출력 데이터 관리**: `input.txt`, `python_output.txt`, `verilog_output.txt` 등의 파일 자동 생성 및 업데이트
- **Testbench 시뮬레이션 실행**: **Icarus Verilog**를 사용하여 Verilog 코드 컴파일 및 시뮬레이션 실행
- **결과 비교를 통한 검증**: Python 스크립트를 활용하여 **Verilog 및 Python에서 Adder의 입출력에 따른 연산 결과 비교** 후 CSV 저장
- **자동 Git 업데이트**: 변경된 파일을 자동으로 GitHub 저장소에 푸시

## ⚙️ 실행 프로세스
1️⃣ **GitHub Actions 실행**
   - cron 스케줄러 또는 수동 실행 (`workflow_dispatch`)

2️⃣ **환경 설정**
   - `actions/checkout@v4`: GitHub 저장소 체크아웃
   - `actions/setup-python@v4`: Python 3.9 설치 및 환경 설정
   - `sudo apt-get install iverilog`: Icarus Verilog 설치

3️⃣ **파일 생성 및 업데이트**
   - `generate_input.py`: `input.txt` 자동 생성
   - GitHub 저장소에 업데이트 (`git add`, `git commit`, `git push`)
   - `run_python_adder.py`: Python으로 Full Adder 실행 (`python_output.txt` 생성 및 GitHub에 업데이트)

4️⃣ **Verilog 실행 및 검증**
   - `iverilog -o adder_sim adder.v adder8.v adder_tb.v`: Verilog 파일 컴파일
   - `vvp adder_sim`: Verilog 시뮬레이션 실행 (`verilog_output.txt` 생성 및 업데이트)

5️⃣ **결과 비교 및 CSV 저장**
   - `compare_files.py`: Python을 이용한 Verilog vs Python 결과 비교
   - `txt_to_csv.py`: 비교 결과를 CSV 파일로 저장 (`comparison_output.csv` 업데이트)
   - GitHub에 최종 결과 업로드 (`git push`)

## 📄 의존성 스크립트 설명
- **generate_input.py**: Verilog 및 Python 시뮬레이션에 필요한 입력 데이터를 생성하여 `input.txt` 파일로 저장
- **run_python_adder.py**: Python으로 Full Adder 로직을 실행하고 결과를 `python_output.txt` 파일에 저장
- **compare_files.py**: Verilog와 Python 실행 결과를 비교하여 검증 작업 수행
- **txt_to_csv.py**: 비교 결과를 CSV 형식의 `comparison_output.csv` 파일로 변환하여 저장
