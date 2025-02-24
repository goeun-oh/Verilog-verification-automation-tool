def is_edge_case(a, b, bit_width):
    """
    주어진 a, b 입력 값이 특정 가산기(bit_width 비트 기준)의 엣지 케이스인지 판별하는 함수.
    결과값을 문자열로 반환.
    """
    max_value = (1 << bit_width) - 1  # 최대값 (예: 4비트면 15)
    min_value = 0  # 최소값 (unsigned 가산기 기준)
    
    # 엣지 케이스 판별
    if a == min_value or b == min_value:
        return f"입력 ({a}, {b}) → 최소값 경계"
    elif a == max_value or b == max_value:
        return f"입력 ({a}, {b}) → 최대값 경계"
    elif a + b > max_value:
        return f"입력 ({a}, {b}) → 오버플로우 발생 가능"
    elif a == b:  # 특이 케이스 (두 입력이 동일할 때)
        return f"입력 ({a}, {b}) → 동일한 입력값 경계"
    
    return f"입력 ({a}, {b}) → 일반 케이스"


# 결과를 input.txt 파일에 저장
with open("input.txt", "w") as file:
    for a, b in test_cases:
        result = is_edge_case(a, b, bit_width)
        file.write(result + "\n")

print("결과가 input.txt 파일에 저장되었습니다.")
