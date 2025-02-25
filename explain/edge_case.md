# 🛠 Edge Case 자동 생성 및 저장

## 📌 개요
이 코드는 **비트 폭(bit-width)에 맞춰 엣지 케이스를 자동 생성**하고, 이를 `input.txt`에 추가 저장하여 Verilog 시뮬레이션을 검증하는 데 활용한다.

---

## 🚀 주요 기능

### ✅ 1. Adder에 사용될 비트 폭 감지
- `number.txt`에서 비트 폭을 읽고 사용

```python
def read_bit_width(file_path="number.txt"):
    try:
        with open(file_path, "r") as file:
            bit_width = int(file.readline().strip())
            return bit_width if bit_width > 0 else 4
    except:
        return 4  # 기본값 4비트
```

### ✅ 2. 숫자 변환 및 오버플로우 체크
- 입력값을 비트 폭에 맞는 이진수로 변환
- 두 수를 더했을 때 최대값 초과 여부를 확인
```python
def binary_format(num, bit_width):
    return format(num, f'0{bit_width}b')

def check_overflow(a, b, bit_width):
    return 1 if (a + b) > ((1 << bit_width) - 1) else 0
```
### ✅ 3. 엣지 케이스 자동 생성
- (0, 0), (최대값, 최대값), (중간값, 중간값+1) 등 특수한 상황을 포함한 테스트 케이스 자동 생성
```python
  def generate_edge_cases(bit_width):
    max_value = (1 << bit_width) - 1
    return [
        (0, 0), (max_value, max_value), (0, max_value),
        (max_value - 1, max_value), (max_value // 2, (max_value // 2) + 1),
        (1, 2), (max_value, 0), (0, 1), (max_value // 2, max_value // 2 + 2)
    ]
```
### ✅ 4. 엣지 케이스를 input.txt에 저장
- 생성된 엣지 케이스를 input.txt에 추가(append) 저장
```python
bit_width = read_bit_width()
test_cases = generate_edge_cases(bit_width)

with open("input.txt", "a") as file:
    for a, b in test_cases:
        file.write(f"{binary_format(a, bit_width)} {binary_format(b, bit_width)} {check_overflow(a, b, bit_width)}\n")

print("엣지 케이스가 input.txt에 저장되었습니다.")
```
