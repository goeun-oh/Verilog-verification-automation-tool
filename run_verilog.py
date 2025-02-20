import subprocess

def run_verilog():
    # 1️. Verilog 코드 컴파일
    # iverilog 설치 필요
    # iverilog로 Verilog 파일 컴파일 testbench.out 생성
    # Verilog 테스트벤치 (testbench.v)
    # Verilog 설계 파일 (dut.v)
    compile_cmd = ["iverilog", "-o", "testbench.out", "testbench.v", "dut.v"]
    result = subprocess.run(compile_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("컴파일 오류 발생!")
        print(result.stderr)
        return
    
    print("Verilog 컴파일 완료!")

    # 2️ 시뮬레이션 실행
    run_cmd = ["vvp", "testbench.out"]
    result = subprocess.run(run_cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("시뮬레이션 실행 완료!")
        print(result.stdout)
    else:
        print("시뮬레이션 오류 발생!")
        print(result.stderr)

if __name__ == "__main__":
    run_verilog()
