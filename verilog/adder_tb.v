module adder_tb;
    reg [15:0] a, b;
    reg cin;
    wire [15:0] sum;
    wire cout;
adder_n uut (
    .a(a), .b(b), .cin(cin), .sum(sum), .cout(cout)
 );

    integer fd_in, fd_out;
    integer scan_result;

    initial begin

        fd_in = $fopen("input.txt", "r");
        fd_out = $fopen("verilog_output.txt", "w");

        if (fd_in == 0) begin
            $display("Error: input.txt file not found.");
            $finish;
        end

        while (!$feof(fd_in)) begin
            scan_result = $fscanf(fd_in, "%b %b %b\n", a, b, cin);
            #10;

            $fwrite(fd_out, "%b %b %b -> sum: %b, cout: %b\n", a, b, cin, sum, cout);
        end

        $fclose(fd_in);
        $fclose(fd_out);
        $finish;
    end
endmodule