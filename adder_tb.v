module adder_tb;
    parameter int MAX_WIDTH = 64;

    // 최대폭으로 선언
    reg  [MAX_WIDTH-1:0] a, b;
    reg                  cin;
    wire [MAX_WIDTH-1:0] sum;
    wire                 cout;

    integer fd_in, fd_bit;
    integer bit_width;
    integer scan_result;

    // adderN 인스턴스: 파라미터를 MAX_WIDTH로
    adderN #(MAX_WIDTH) uut (
        .a(a),
        .b(b),
        .cin(cin),
        .sum(sum),
        .cout(cout)
    );

    initial begin
        // 1) number.txt에서 bit_width 읽기
        fd_bit = $fopen("number.txt", "r");
        if (fd_bit == 0) begin
            $display("ERROR: Could not open number.txt");
            $finish;
        end
        scan_result = $fscanf(fd_bit, "%d", bit_width);
        $fclose(fd_bit);

        if (bit_width > MAX_WIDTH) begin
            $display("ERROR: bit_width(%0d) > MAX_WIDTH(%0d)", bit_width, MAX_WIDTH);
            $finish;
        end

        // 2) input.txt 열기
        fd_in = $fopen("input.txt", "r");
        if (fd_in == 0) begin
            $display("ERROR: Could not open input.txt");
            $finish;
        end

        // 3) 파일 끝까지 읽어서 시뮬레이션
        while (!$feof(fd_in)) begin
            // input.txt에는 bit_width만큼의 a, b(이진), 그리고 cin(1비트)이 있다고 가정
            scan_result = $fscanf(fd_in, "%b %b %b\n",
                                  a[bit_width-1:0],  // 하위 bit_width만 읽어서 a에 저장
                                  b[bit_width-1:0],
                                  cin);
            #10;  // 시뮬레이션 시간 경과

            $display("Read: a=%b b=%b cin=%b => sum=%b cout=%b (bit_width=%0d)",
                     a[bit_width-1:0], b[bit_width-1:0], cin,
                     sum[bit_width-1:0], cout, bit_width);
        end

        $fclose(fd_in);
        $finish;
    end
endmodule
