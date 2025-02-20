`timescale 1ns / 1ps

module adder_tb;

    reg a, b, cin;
    wire sum, cout;
    integer file, scan_result;
    parameter input_file ="input_vectors.txt";


    // Full Adder 인스턴스 생성
    adder uut (
        .a(a), 
        .b(b), 
        .cin(cin), 
        .sum(sum), 
        .cout(cout)
    );

    initial begin

        $dumpfile("test_out2.vcd");  // VCD 파일 생성
        $dumpvars;  // 전체 신호 저장
        // 입력 벡터 파일 열기
        file = $fopen(input_file, "r");
        if (file == 0) begin
            $display(" Error: not exist %s file", input_file);
            $finish;
        end
        
        $display("\n");
        $display("read %s data ...\n", input_file);
        $display(" a | b | cin | sum | cout ");
        $display("-------------------------");

        // 파일에서 한 줄씩 읽어서 테스트 실행
        while (!$feof(file)) begin
            scan_result = $fscanf(file, "%d %d %d\n", a, b, cin);
            #1;  // 1ns 대기 (Full Adder 연산 실행)
            $display(" %b | %b |  %b  |  %b  |  %b  ", a, b, cin, sum, cout);
        end

        // 파일 닫기
        $fclose(file);
        $finish;
    end

endmodule
