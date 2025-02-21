import random
import os

bit = 8
NUM_TEST_CLASS = 2 ** bit

def translate_2bit(num):
    binary = [0] * bit
    for i in range(bit):
        binary[bit - 1 - i] = num % 2
        num //= 2
    return binary

def generate_data():
    data = []
    while(1):  # 6개의 데이터 라인 생성
        a = random.randint(0, NUM_TEST_CLASS - 1)
        b = random.randint(0, NUM_TEST_CLASS - 1)
        a_2bit = translate_2bit(a)
        b_2bit = translate_2bit(b)
        result = random.randint(0, 1)  # 결과값을 0 또는 1로 랜덤 지정
        data.append((a_2bit, b_2bit, result))
    return data

def write_to_file(data, filename="input.txt"):
    with open(filename, "w") as file:
        for a_2bit, b_2bit, result in data:
            a_str = "".join(map(str, a_2bit))
            b_str = "".join(map(str, b_2bit))
            file.write(f"{a_str} {b_str} {result}\n")

data = generate_data()
write_to_file(data)
