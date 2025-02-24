# 🛠 Edge Case 자동 생성 및 입력 파일 저장

## 📌 개요
이 코드는 **비트 폭(bit-width)에 맞춰 엣지 케이스를 자동 생성**하고, 이를 `input.txt`에 추가하는 기능을 수행한다.  
Verilog 시뮬레이션을 수행하기 전, **예상치 못한 corner case(특수한 상황)에서 발생할 수 있는 문제를 탐지**하기 위해 사용된다.

---

## 🚀 주요 기능

### ✅ 1. **비트 폭(bit-width) 읽기**
- `number.txt`에서 가산기의 비트 폭을 읽어온다.
- 값이 없거나 비정상적인 경우 **기본값(4비트)** 을 사용한다.

```python
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
