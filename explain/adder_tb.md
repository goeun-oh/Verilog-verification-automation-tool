# 📌 N Bit 가산기 TestBench
---

## 🚀 주요 기능
  - adder_tb.v: 입력 txt 파일을 읽어와서 입력(a, b, cin), 출력(cout, sum)값 테스트
---

### ✅ testbench 실행 (adder_tb.v)
📌 **기능 상세**
  - python(generate_tb.py)에서 bit width를 입력받고, adder_tb.v 자동 생성
    
  - file = $fopen("input_txt", "r")로 입력 txt 파일 read 후, 변수에 할당
    1. if (fd_in == 0) 이면 Error 메세지 출력 후 종료
    2. file이 존재한다면 다음 로직
   
  - $fscanf(file, "%d %d %d\n", a, b, cin)로 파일 한 줄씩 읽고 테스트 실행
    1. 각 연산당 1ns 실행
    2. 테스트 후, $display로 값 출력

  - $fwrite(fd_out, "%b %b %b -> sum: %b, cout: %b\n", a, b, cin, sum, cout)로 fd_out에 write
    1. verilog_output.txt 생성
    
  - $fclose(file)로 파일 닫기
