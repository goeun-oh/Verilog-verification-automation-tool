# 🔢n-bit Full Adder 설계 자동화
1-bit 가산기 모듈인 `adder.v` 를 bit width 만큼 인스턴스하여 n-bit full adder를 자동으로 설계합니다.
이를 위해, 1-bit 가산기 모듈인 `adder.v`가 정의되어 있어야합니다.


## 🚀주요 기능
- Python을 활용하여 Verilog 기반의 n-bit Full Adder 모듈과 테스트벤치를 자동 생성함.
- 사용자가 원하는 비트 수에 맞춰 Full Adder 설계를 자동화.
- 생성된 Verilog 파일을 이용해 하드웨어 설계 및 검증 가능.

## 🛠구성 요소
### 1️⃣ Verilog 모듈 생성 (generate_vfile.py)
- **adder_n 모듈**: 입력 `a`, `b`, `cin`을 받아 `sum`과 `cout`을 출력하는 n-bit Full Adder.
- **구성 방식**:
  - `adder`라는 기본 단위에서 Full Adder를 조합하여 n-bit 연산을 수행.
  - `carry` 신호를 이용해 각 비트 연산을 연결함.
- **코드 요약**:
  ```verilog
  module adder_n (input [N-1:0] a, input [N-1:0] b, input cin, output [N-1:0] sum, output cout);
      wire [N-1:0] carry;
      adder FA0 (a[0], b[0], cin, sum[0], carry[0]);
      ...
      adder FA(N-1) (a[N-1], b[N-1], carry[N-2], sum[N-1], cout);
  endmodule
  ```

### 2️⃣ 테스트벤치 생성 (generate_tb.py)
- **adder_tb 모듈**: `adder_n` 모듈을 테스트하는 벤치마크 코드 자동 생성.
- **파일 입출력 기반 테스트**:
  - `input.txt`에서 테스트 데이터를 읽어 `adder_n` 모듈 실행.
  - `verilog_output.txt`에 결과를 저장하여 검증 가능.
- **코드 요약**:
  ```verilog
  module adder_tb;
      reg [N-1:0] a, b;
      reg cin;
      wire [N-1:0] sum;
      wire cout;
      adder_n uut ( .a(a), .b(b), .cin(cin), .sum(sum), .cout(cout) );
      ...
  endmodule
  ```

## 사용 방법
1. `number.txt` 파일에 원하는 비트 수를 입력.
2. `generate_vfile.py` 실행 → `adder_n.v` 파일 생성.
3. `generate_tb.py` 실행 → `adder_tb.v` 파일 생성.
4. `adder_tb.v`를 실행하여 결과 확인.
