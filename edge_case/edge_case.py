def read_bit_width(file_path="number.txt"):
    """
    number.txt에서 가산기의 비트 폭을 읽어오는 함수.
    """
    try:
        with open(file_path, "r") as file:
            bit_width = int(file.readline().strip())  # 첫 줄의 숫자를 읽음
            if bit_width <= 0:
                raise ValueError("비트 폭은 1 이상이어야 합니다.")
            return bit_width
    except Exception as e:
        print(f"비트 폭을 읽는 중 오류 발생: {e}")
        return 4  # 기본값: 4비트

def binary_format(num, bit_width):
    """주어진 숫자를 bit_width 비트의 이진수 문자열로 변환"""
    return format(num, f'0{bit_width}b')

def check_overflow(a, b, bit_width):
    """두 값을 더했을 때 오버플로우(1) 여부를 판별"""
    max_value = (1 << bit_width) - 1  # 최대값 (예: 4비트면 15)
    return 1 if (a + b) > max_value else 0

def generate_edge_cases(bit_width):
    """
    비트 폭에 맞춰 엣지 케이스를 자동 생성하는 함수
    """
    max_value = (1 << bit_width) - 1  # 최대값 (예: 4비트면 15)
    min_value = 0  # 최소값 (unsigned 기준)

    return [
        (min_value, min_value),  # (0, 0) 최소값
        (max_value, max_value),  # (최대값, 최대값)
        (min_value, max_value),  # (0, 최대값)
        (max_value - 1, max_value),  # (최대값-1, 최대값)
        (max_value // 2, (max_value // 2) + 1),  # (중간값, 중간값+1) 연속된 값
        (1, 2),  # 작은 연속된 값
        (max_value, 0),  # (최대값, 최소값)
        (0, 1),  # (0, 1) 최소값과 연속값
        (max_value // 2, max_value // 2 + 2),  # (중간값, 중간값+2) 오버플로우 가능 케이스
    ]

# 비트 폭을 number.txt에서 읽어옴
bit_width = read_bit_width()

# 자동으로 엣지 케이스를 생성
test_cases = generate_edge_cases(bit_width)

# 결과를 input.txt 파일에 **엣지 케이스만 추가 저장 (append)**
with open("input.txt", "a") as file:
    for a, b in test_cases:
        a_bin = binary_format(a, bit_width)  # A를 이진수 변환
        b_bin = binary_format(b, bit_width)  # B를 이진수 변환
        overflow_flag = check_overflow(a, b, bit_width)  # 오버플로우 판별
        file.write(f"{a_bin} {b_bin} {overflow_flag}\n")

print("엣지 케이스 분석 결과가 input.txt 파일에 추가 저장되었습니다.")
