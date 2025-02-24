def is_edge_case(a, b, bit_width):
    """
    주어진 a, b 입력 값이 특정 가산기(bit_width 비트 기준)의 엣지 케이스인지 판별하는 함수.

    - 최소값, 최대값, 오버플로우 발생 가능 값 등을 확인함.
    """
    max_value = (1 << bit_width) - 1  # 최대값 (예: 4비트면 15)
    min_value = 0  # 최소값 (unsigned 가산기 기준)
    
    # 엣지 케이스 판별
    if a == min_value or b == min_value:
        return "최소값 경계"
    elif a == max_value or b == max_value:
        return "최대값 경계"
    elif a + b > max_value:
        return "오버플로우 발생 가능"
    elif a == b:  # 특이 케이스 (두 입력이 동일할 때)
        return "동일한 입력값 경계"
    
    return "일반 케이스"
