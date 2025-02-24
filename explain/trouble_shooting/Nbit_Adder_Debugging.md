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
- **기존 방식은 1 bit adder 8개를 모듈화하여 연결하는 방식**
  1. parameter n에 따라 N bit로 확장할 때 어떤 방식으로 코드를 작성할 것인가?
     1. verilog에서 모든 Bit가 적용가능한 Add 연산식 구현 -> 부정확한 연산 값의 문제 발생
     2. python에서 v 파일 write 과정에서 반복문 최적화를 통해 모든 n bit에 적용가능한 코드 작성 **(해당 방식을 채택)**

<br>

📌 **최적화한 generate_vfile.py**
  ```python
def gen_v(v, bit_width):
    with open(v, "w") as v:
        v.write(f"module adder_n (input [{bit_width-1}:0] a, input [{bit_width-1}:0] b, input cin, output [{bit_width-1}:0] sum, output cout);\n")
        v.write(f"    wire [{bit_width-1}:0] carry;\n\n")
        v.write(f"    adder FA0 (a[0], b[0], cin, sum[0], carry[0]);\n")
        for i in range(bit_width-2):
            v.write(f"    adder FA{i+1} (a[{i+1}], b[{i+1}], carry[{i}], sum[{i+1}], carry[{i+1}]);\n")
        v.write(f"    adder FA{bit_width-1} (a[{bit_width-1}], b[{bit_width-1}], carry[{bit_width-2}], sum[{bit_width-1}], cout);\n")
        v.write("endmodule")
        
        
def fetch_num():
    with open("number.txt","r") as f:
        bit_width=int(f.read().strip())
    return bit_width
    
    
    
bit_width=fetch_num()
gen_v("adder_n.v", bit_width)
```

<br>

📌 **최적화한 generate_tb.py**
  ```python
def gen_tb(tb, bit_width):
    instance_lines = ["adder_n uut (\n", "    .a(a), .b(b), .cin(cin), .sum(sum), .cout(cout)\n", " );\n\n" ]
    file_lines=["    integer fd_in, fd_out;\n", "    integer scan_result;\n", "\n"]
    initial_lines=["    initial begin\n\n", '        fd_in = $fopen("input.txt", "r");\n','        fd_out = $fopen("verilog_output.txt", "w");\n\n', ]
    is_fdin=["        if (fd_in == 0) begin\n", '            $display("Error: input.txt file not found.");\n', "            $finish;\n", "        end\n\n"]
    is_input_end=["        while (!$feof(fd_in)) begin\n", '            scan_result = $fscanf(fd_in, "%b %b %b\\n", a, b, cin);\n', "            #10;\n\n", '            $fwrite(fd_out, "%b %b %b -> sum: %b, cout: %b\\n", a, b, cin, sum, cout);\n', '        end\n\n']
    file_close=["        $fclose(fd_in);\n", "        $fclose(fd_out);\n", "        $finish;\n"]
    line_end=["    end\n", "endmodule"]
    
    with open(tb, "w") as tb:
        tb.write("module adder_tb;\n")
        tb.write(f"    reg [{bit_width-1}:0] a, b;\n")
        tb.write(f"    reg cin;\n")
        tb.write(f"    wire [{bit_width-1}:0] sum;\n")
        tb.write(f"    wire cout;\n")
        tb.writelines(instance_lines)
        tb.writelines(file_lines)
        tb.writelines(initial_lines)
        tb.writelines(is_fdin)
        tb.writelines(is_input_end)
        tb.writelines(file_close)
        tb.writelines(line_end)
        
        
        

        
def fetch_num():
    with open("number.txt","r") as f:
        bit_width=int(f.read().strip())
    return bit_width
    
    
    
bit_width = fetch_num()
gen_tb("adder_tb.v", bit_width)
```

 - adder_n.v와 adder_tb.v 로직을 python 반복문 최적화로 구현
   1. verilog 연산 로직 재구성 없이 모든 bit에 대한 연산 가능
   2. 연산 로직 일반화로 예상치 못한 error case 최소화 
