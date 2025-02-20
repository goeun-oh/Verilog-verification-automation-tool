# generate_input.py
import random
import os

NUM_TEST_CLASS = 2*2*2

def generate_input_data(NUM_TEST_CLASS):
    with open("input.txt", "w") as file:
        for i in range(NUM_TEST_CLASS):
            A = random.randint(0,1)
            B = random.randint(0,1)
            Cin =random.randint(0,1)
            file.write(f"{A} {B} {Cin}\n")
    print(f"✅ {NUM_TEST_CLASS}개 입력 데이터 생성 완료! ({INPUT_FILE})")

if __name__ == "__main__":
    generate_input_data(NUM_TEST_CLASS)
