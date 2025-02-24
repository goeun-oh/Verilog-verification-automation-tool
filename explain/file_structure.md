# 📂 파일 구조 및 프로젝트 흐름
📦 Verilog-verification-automation-tool <br>
 ┣ 📜 `README.md`                  # 전체 프로젝트 설명 파일 <br>
 ┣ 📂 `explain`            <br>
 ┗ ┗ 📜 `file_structure.md`        # file 구조 설명 <br>

 1️⃣ testcase / n-bit verilog, tb file 자동 생성 <br>
 ┣ 📜 `number.txt`                 # bit width 를 저장 <br>
 ┣ 📜 `generate_vfile.py`          # `number.txt` 에 저장된 정수(n)을 바탕으로 n-bit adder 모듈 자동 생성 <br>
 ┣ 📜 `generate_tb.py`             # `number.txt` 에 저장된 정수(n)을 바탕으로 n-bit adder testbench 모듈 자동 생성 <br>
 ┣ 📜 `generate_input.py`          # n-bit 를 가지는 random input 6개를 생성하여 `input.txt` 에 저장 <br>
 ┗ 📜 `input.txt`                  

 2️⃣ Verilog 코드 <br>
 ┣ 📜 `adder.v`                    # Verilog 1 bit Full Adder <br>
 ┣ 📜 `adder_n.v`                  # `generate_vfile.py`에 의해 자동생성된 Verilog n bit Full Adder 모듈 <br>
 ┣ 📜 `adder_tb.v`                 # `generate_tb.py`에 의해 자동생성된 Verilog Testbench 모듈 <br>
 ┗ 📜 `verilog_output.txt`         # `input.txt`를 input으로 하는 n-bit Full Adder(Verilog) 연산 결과 저장 <br>

 3️⃣ Python 연산 및 결과 저장 <br>
 ┣ 📜 `run_python_adder.py`        # n-bit 덧셈을 파이썬 환경에서 실행하는 파일 <br>
 ┣ 📜 `python_output.txt`          # `input.txt`를 input으로 하는 n-bit 덧셈기(Python) 연산 결과 저장 <br>

 4️⃣ 결과 비교 및 검증 <br>
 ┣ 📜 `compare_files.py`           # Python과 Verilog 결과 비교 스크립트 <br>
 ┣ 📜 `txt_to_csv.py`              # `compare_files.py`의 결과를 csv 형식으로 저장 <br>
 ┣ 📜 `comparision_output.csv`
 ┣ 📜 `success_per.py`             # 누적된 testcase에 대한 성공률 계산 <br>
 ┣ 📜 `success_per.txt`            # testcase 누적 성공률 저장 <br>
 ┣ 📂 `.github/workflows`          # GitHub Actions 워크플로우 파일 저장소 <br>
 ┗ ┗ 📜 `verilog_verification.yml` # GitHub Actions 자동화 스크립트 <br>
