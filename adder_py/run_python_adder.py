import os

def full_adder_variable_width(a, b, cin, bit_width):
    """가변 비트 Full Adder 연산 수행"""
    sum_out = 0
    cout = cin

    for i in range(bit_width):
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
        sum_bit = (bit_a ^ bit_b) ^ cout
        cout = (bit_a & bit_b) | (cout & (bit_a ^ bit_b))
        sum_out |= (sum_bit << i)

    return sum_out, cout

def run_python_adder():
    """Python에서 가변 비트 Full Adder 실행 및 결과 저장"""
    # 1) number.txt에서 비트 수 읽어오기
    with open("number.txt", "r") as f:
        bit_width = int(f.read().strip())

    results = []

    # 2) input.txt에서 입력 데이터 읽어서 연산
    with open("input.txt", "r") as f:
        inputs = [line.strip().split(" ") for line in f.readlines()]

    for in_values in inputs:
        A = int(in_values[0], 2)  # 2진수 문자열 -> 정수
        B = int(in_values[1], 2)
        Cin = int(in_values[2])

        Sum, Cout = full_adder_variable_width(A, B, Cin, bit_width)

        # sum을 bit_width만큼의 이진수로 표현
        sum_str = format(Sum, f'0{bit_width}b')

        results.append(f"{in_values[0]} {in_values[1]} {in_values[2]} -> sum: {sum_str}, cout: {Cout}")

    # 3) 결과를 파일로 저장
    output_file = "python_output.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(results))

    print(f"✅ Python {bit_width}-bit Full Adder 연산 완료! 결과가 '{output_file}'에 저장되었습니다.")

# 실행
run_python_adder()
