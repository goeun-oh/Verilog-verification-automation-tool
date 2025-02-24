module adder_tb;
    // 최대 비트 수를 정해둔다. (필요에 따라 64 등으로 설정 가능)
    parameter int MAX_WIDTH = 64;

    // 우선 레지스터(또는 logic) 신호를 최대 폭으로 잡아둔다.
    // 실제로는 number.txt에서 읽은 bit_width만큼만 유효하게 쓸 것이다.
    logic [MAX_WIDTH-1:0] a, b;
    logic cin;
    logic [MAX_WIDTH-1:0] sum;
    logic cout;

    // 동적으로 읽은 bit_width를 저장할 변수
    integer bit_width;

    // adder 인스턴스 (여기서는 일단 최대폭으로 연결해 두고, 실제 사용은 부분선택으로 처리)
    adder #(MAX_WIDTH) uut (
        .a(a),
        .b(b),
        .cin(cin),
        .sum(sum),
        .cout(cout)
    );

    integer fd_in, fd_out;
    integer fd_bit;
    integer scan_result;

    initial begin
        // 1) number.txt에서 비트 수 읽어오기
        fd_bit = $fopen("number.txt","r");
        if (fd_bit == 0) begin
            $display("Error: number.txt file not found.");
            $finish;
        end
        scan_result = $fscanf(fd_bit, "%d", bit_width);
        $fclose(fd_bit);

        // 만약 읽어온 bit_width가 MAX_WIDTH를 초과하면 종료
        if (bit_width > MAX_WIDTH) begin
            $display("Error: bit_width(%0d) > MAX_WIDTH(%0d).", bit_width, MAX_WIDTH);
            $finish;
        end

        // 2) input.txt 열어서 시뮬레이션용 데이터 읽어오기
        fd_in = $fopen("input.txt", "r");
        fd_out = $fopen("verilog_output.txt", "w");

        if (fd_in == 0) begin
            $display("Error: input.txt file not found.");
            $finish;
        end

        // 3) 파일 끝까지 데이터 반복 읽기
        while (!$feof(fd_in)) begin
            // 가변 부분 선택(variable part-select)을 사용해,
            // input.txt에는 bit_width만큼의 a, b, 그리고 cin(1bit) 순서로 들어있다고 가정
            scan_result = $fscanf(fd_in, "%b %b %b\n", a[bit_width-1:0], b[bit_width-1:0], cin);
            #10; // 연산 대기

            // 출력도 sum[bit_width-1:0] 범위를 실제 유효 결과로 간주
            $fwrite(fd_out, 
                "%0dbit => a:%b b:%b cin:%b -> sum:%b, cout:%b\n", 
                bit_width, 
                a[bit_width-1:0], 
                b[bit_width-1:0], 
                cin,
                sum[bit_width-1:0], 
                cout
            );
        end

        $fclose(fd_in);
        $fclose(fd_out);
        $finish;
    end
endmodule
