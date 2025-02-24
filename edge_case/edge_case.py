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
    """
    주어진 숫자를 bit_width 비트의 이진수 문자열로 변환.
    """
    return format(num, f'0{bit_width}b')

def check_overflow(a, b, bit_width):
    """
    두 값을 더했을 때 오버플로우(1) 여부를 판별.
    """
    max_value = (1 << bit_width) - 1  # 최대값 (예: 4비트면 15)
    return 1 if (a + b) > max_value else 0

def is_edge_case(a, b, bit_width):
    """
    엣지 케이스 여부 판별 (해당하는 경우 True 반환)
    """
    max_value = (1 << bit_width) - 1  # 최대값 (예: 4비트면 15)
    min_value = 0  # 최소값 (unsigned 기준)
    
    # 엣지 케이스 조건
    if a == min_value or b == min_value:  # 최소값 경계
        return True
    if a == max_value or b == max_value:  # 최대값 경계
        return True
    if a + b > max_value:  # 오버플로우 발생
        return True
    if a == max_value - 1 or b == max_value - 1:  # 최대값 직전 경계
        return True
    if abs(a - b) == 1:  # 연속된 입력값 경계
        return True

    return False  # 일반 케이스

# 비트 폭을 number.txt에서 읽어옴
bit_width = read_bit_width()

# 테스트 케이스 (엣지 케이스 확인을 위해 후보들 선정)
test_cases = [
    (0, 0), (15, 15), (0, 15), (7, 8), (10, 6),  
    (14, 15), (1, 2), (15, 0), (0, 1), (7, 9)
]

# 결과를 input.txt 파일에 **엣지 케이스만 추가 저장 (append)**
with open("input.txt", "a") as file:
    for a, b in test_cases:
        if is_edge_case(a, b, bit_width):  # 엣지 케이스인 경우만 저장
            a_bin = binary_format(a, bit_width)  # A를 이진수 변환
            b_bin = binary_format(b, bit_width)  # B를 이진수 변환
            overflow_flag = check_overflow(a, b, bit_width)  # 오버플로우 판별
            file.write(f"{a_bin} {b_bin} {overflow_flag}\n")

print("엣지 케이스 분석 결과가 input.txt 파일에 추가 저장되었습니다.")
