def generate_full_adder_edge_cases(n):
    max_value = (1 << n) - 1
    edge_cases = [
        (0, 0, 0),
        (max_value, 0, 0),
        (0, max_value, 0),
        (max_value, 1, 0),
        (1, max_value, 0),
        (max_value, max_value, 1),
        (max_value // 2, max_value // 2 + 1, 0),
        (1 << (n-1), 1 << (n-1), 1),
        (max_value - 1, 1, 0),
        (1 << (n-1) - 1, 1, 1)
    ]
    return edge_cases

def format_binary(num, n):
    return f"{num:0{n}b}"

def create_input_file(n):
    cases = generate_full_adder_edge_cases(n)
    filename = 'input.txt'
    
    with open(filename, 'w') as f:
        f.write(f"{n}\n")
        f.write(f"{len(cases)}\n")
        for a, b, cin in cases:
            f.write(f"{format_binary(a, n)} {format_binary(b, n)} {cin}\n")
    
    print(f"{filename} 파일이 생성되었습니다.")

n = int(input("Full adder의 비트 수를 입력하세요: "))
create_input_file(n)
