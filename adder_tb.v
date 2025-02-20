module adder_tb;
    reg a, b, cin;
    wire sum, cout;
    
    adder uut (
        .a(a), .b(b), .cin(cin), .sum(sum), .cout(cout)
    );

    integer fd_in, fd_out;
    integer scan_result;

    initial begin
        fd_in = $fopen("input.txt", "r"); // 입력 파일 열기
        fd_out = $fopen("output.txt", "w"); // 출력 파일 열기

        if (fd_in == 0) begin
            $display("Error: input.txt file not found.");
            $finish;
        end

        $fwrite(fd_out, "A B Cin | Sum Cout\n"); // 결과 헤더 작성

        while (!$feof(fd_in)) begin
            scan_result = $fscanf(fd_in, "%b %b %b\n", a, b, cin); // input.txt에서 데이터 읽기
            #10; // 연산 대기

            $fwrite(fd_out, "%b %b %b | %b %b\n", a, b, cin, sum, cout); // 결과 저장
        end

        $fclose(fd_in);
        $fclose(fd_out);
        $finish;
    end
endmodule
