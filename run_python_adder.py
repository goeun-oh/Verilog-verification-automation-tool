def full_adder_8bit(a, b, cin):
    """8-bit Full Adder 연산 수행"""
    sum_out = 0
    cout = cin  # 초기 carry 값 설정

    for i in range(8):  # 8비트 처리
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
        sum_bit, cout = (bit_a ^ bit_b) ^ cout, (bit_a & bit_b) | (cout & (bit_a ^ bit_b))
        sum_out |= (sum_bit << i)

    return sum_out, cout

def run_python_adder():
    """Python에서 8-bit Full Adder 실행 및 결과 저장"""
    results = []

    # `input.txt`에서 입력 데이터 읽기
    with open("input.txt", "r") as f:
        inputs = [line.strip().split(" ") for line in f.readlines()]

    for in_values in inputs:
        A = int(in_values[0], 2)  # 2진수 문자열을 정수로 변환
        B = int(in_values[1], 2)
        Cin = int(in_values[2])
        Sum, Cout = full_adder_8bit(A, B, Cin)

        # 결과를 8비트 바이너리 문자열로 변환 후 저장
        results.append(f"{in_values[0]} {in_values[1]} {in_values[2]} -> sum: {Sum:08b}, cout: {Cout}")

    # Python 연산 결과 저장
    output_file = "python_output.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(results))

    print(f"✅ Python 8-bit Full Adder 연산 완료! 결과가 '{output_file}'에 저장되었습니다.")

run_python_adder()
