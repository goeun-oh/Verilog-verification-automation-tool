# 📌 8 Bit -> N Bit로 모듈 확장
---

## 🚀 주요 기능
  - generate_vfile.py : bit-width에 따라 다양한 bit의 add 연산을 할 수 있는 v 파일 생성
  - generate_tb.py : bit-width에 따라 다양한 bit의 add 연산을 할 수 있는 tb 파일 생성
    1. adder_n.v 생성
    2. adder_tb.v 생성
---

### ✅ trouble shooting
📌 **수정 전 adder_8bit.v**
  ```python
module adder_8bit (input [7:0] a, input [7:0] b, input cin, output [7:0] sum, output cout);
    wire [7:0] carry;
    
    adder FA0 (a[0], b[0], cin, sum[0], carry[0]);
    adder FA1 (a[1], b[1], carry[0], sum[1], carry[1]);
    adder FA2 (a[2], b[2], carry[1], sum[2], carry[2]);
    adder FA3 (a[3], b[3], carry[2], sum[3], carry[3]);
    adder FA4 (a[4], b[4], carry[3], sum[4], carry[4]);
    adder FA5 (a[5], b[5], carry[4], sum[5], carry[5]);
    adder FA6 (a[6], b[6], carry[5], sum[6], carry[6]);
    adder FA7 (a[7], b[7], carry[6], sum[7], cout);
endmodule
```
- 기존 방식은 1 bit adder 8개를 모듈화하여 연결하는 방식
  1. parameter n에 따라 N bit로 확장할 때 어떤 방식으로 코드를 작성할 것인가?
     1. ㄷㄷ  
