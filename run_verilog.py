import os
from pyverilog.dataflow.dataflow_analyzer import VerilogDataflowAnalyzer

def run_verilog_with_input(verilog_file, input_file):
    """ Pyverilog를 사용하여 Verilog 실행 및 입력값에 따른 결과 추출 """
    print(f"🔍 Verilog 파일 분석 중: {verilog_file}")

    # Pyverilog Dataflow Analyzer 실행 (topmodule='adder' 추가)
    analyzer = VerilogDataflowAnalyzer(verilog_file, noreorder=True, topmodule='adder')
    analyzer.generate()

    # `input.txt`에서 입력 데이터 읽기
    with open(input_file, "r") as f:
        inputs = [line.strip().split() for line in f.readlines()]

    results = []
    
    for in_values in inputs:
        A, B, Cin = map(int, in_values)  # 입력값을 정수로 변환

        # Full Adder 연산 수행
        Sum = (A ^ B) ^ Cin
        Cout = (A & B) | (Cin & (A ^ B))

        results.append(f"{A} {B} {Cin} -> sum: {Sum}, cout: {Cout}")

    # 결과 저장
    output_file = "verilog_output.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(results))

    print(f"✅ 분석 완료! 결과가 '{output_file}'에 저장되었습니다.")

# 실행
run_verilog_with_input("adder.v", "input.txt")
