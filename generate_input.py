import random

NUM_TEST_CLASS = 2*2*2  # 테스트 데이터 개수
INPUT_FILE = "input.txt"

def generate_input_data(num_tests):
    with open(INPUT_FILE, "w") as file:
        for _ in range(num_tests):
            A = random.randint(0, 1)
            B = random.randint(0, 1)
            Cin = random.randint(0, 1)
            file.write(f"1'b{A} 1'b{B} 1'b{Cin}\n")  # Verilog 호환 형식으로 저장
    print(f"{num_tests}개 입력 데이터 생성 완료! ({INPUT_FILE})")

if __name__ == "__main__":
    generate_input_data(NUM_TEST_CLASS)
