`timescale 1ns / 1ps

module adder_tb;

    reg a, b, cin;
    wire sum, cout;
    integer file, scan_result;

    // Full Adder 인스턴스 생성
    Full_adder uut (
        .a(a), 
        .b(b), 
        .cin(cin), 
        .sum(sum), 
        .cout(cout)
    );

    initial begin
        // 입력 벡터 파일 열기
        file = $fopen("input_vectors.txt", "r");
        if (file == 0) begin
            $display("❌ Error: input_vectors.txt 파일을 찾을 수 없습니다.");
            $finish;
        end
        
        $display("✅ input_vectors.txt에서 입력 벡터를 읽어옵니다.");
        $display(" a | b | cin | sum | cout ");
        $display("-------------------------");

        // 파일에서 한 줄씩 읽어서 테스트 실행
        while (!$feof(file)) begin
            scan_result = $fscanf(file, "%d %d %d\n", a, b, cin);
            #10;  // 10ns 대기 (Full Adder 연산 실행)
            $display(" %b | %b |  %b  |  %b  |  %b  ", a, b, cin, sum, cout);
        end

        // 파일 닫기
        $fclose(file);
        $finish;
    end

endmodule
