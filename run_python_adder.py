def full_adder(a, b, cin):
    """Full Adder 연산 수행"""
    sum_out = (a ^ b) ^ cin
    cout_out = (a & b) | (cin & (a ^ b))
    return sum_out, cout_out

def run_python_adder():
    """Python에서 Full Adder 실행 및 결과 저장"""
    results = []

    # `input.txt`에서 입력 데이터 읽기
    with open("input.txt", "r") as f:
        inputs = [line.strip().split() for line in f.readlines()]

    for in_values in inputs:
        A=int(in_values[0])
        B=int(in_values[1])
        Cin=int(in_values[2])
        Sum, Cout=full_adder(A,B,Cin)
        results.append(f"{A} {B} {Cin} -> sum: {Sum}, cout: {Cout}")

    # Python 연산 결과 저장
    output_file = "python_output.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(results))

    print(f"✅ Python 연산 완료! 결과가 '{output_file}'에 저장되었습니다.")
    
run_python_adder()

