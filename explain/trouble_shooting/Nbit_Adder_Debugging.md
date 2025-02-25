## 📌 8 Bit -> N Bit로 모듈 확장
---
### 🛠 문제
- 가산기 동작 검증을 위해 8-bit Adder를 설계, 무작위 입력 값에 대해 정상 작동함을 확인
- bit 수가 늘어나도 정상 작동하는지 테스트할 필요를 느낌
- 기존 처럼 일일이 가산기 모듈과 testbench 모듈을 작성하는 것이 아닌, bit 수만 선택한다면 자동으로 모듈과 testbench 모듈을 생성해주는 모델 설계를 고민하게됨
 
## 🚀 주요 기능
  - generate_vfile.py : bit-width에 따라 다양한 bit의 add 연산을 할 수 있는 v 파일 생성
  - generate_tb.py : bit-width에 따라 다양한 bit의 add 연산을 할 수 있는 tb 파일 생성
    1. adder_n.v 생성
    2. adder_tb.v 생성
---


### ✅ 해결 방법
- bit 폭을 선택하는 `number.txt`파일을 생성
- `number.txt` 에 담긴 정수(**n**)을 읽어 n-bit Adder 모듈과 테스트벤치를 자동 생성하는 python file 작성(`generate_vfile.py`, `generate_tb.py`)

### 🎯 결과
- verilog 연산 로직 재구성 없이 모든 bit에 대한 연산 가능
- 정수(**n**)만 선택하면 가산기 모듈 및 테스트벤치 자동 생성
- 연산 로직 일반화로 예상치 못한 error case 최소화 
