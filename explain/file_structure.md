# 📂 파일 구조 및 프로젝트 흐름
📦 Verilog-verification-automation-tool <br>
 ┣ 📜 `README.md`                  # 전체 프로젝트 설명 파일 <br>
 ┣ 📂 `explain`            <br>
 ┗ ┗ 📜 `file_structure.md`        # file 구조 설명 <br>

 1️⃣ 입력 데이터 생성 <br>
 ┣ 📜 `generate_input.py`          # random input을 생성하여 input.txt 에 저장 <br>
 ┣ 📜 `input.txt`                  # Full Adder 테스트 입력값 <br>

 2️⃣ Verilog 코드 <br>
 ┣ 📜 `adder.v`                    # Verilog 1 bit Full Adder <br>
 ┣ 📜 `adder_n.v`                  # Verilog n bit Full Adder <br>
 ┣ 📜 `adder_tb.v`                 # Verilog Testbench <br>
 ┣ 📜 `verilog_output.txt`         # Verilog 실행 결과 저장 <br>

 3️⃣ Python 연산 및 결과 저장 <br>
 ┣ 📜 `run_python_adder.py`        # Python에서 Full Adder 실행 및 결과 저장 <br>
 ┣ 📜 `python_output.txt`          # Python 연산 결과 저장 <br>

 4️⃣ 결과 비교 및 검증 <br>
 ┣ 📜 `compare_files.py`           # Python과 Verilog 결과 비교 스크립트 <br>
 ┣ 📜 `txt_to_csv.py`              # compare_files.py의 결과를 csv 형식으로 저장 <br>
 ┣ 📜 `comparision_output.csv`     # 저장된 csv 파일 <br>
 ┣ 📂 .github/workflows            # GitHub Actions 워크플로우 파일 저장소 <br>
 ┗ ┗ 📜 `verilog_verification.yml` # GitHub Actions 자동화 스크립트 <br>
