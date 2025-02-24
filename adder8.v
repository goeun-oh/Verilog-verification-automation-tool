module adder8 (input [3:0] a, input [3:0] b, input cin, output [3:0] sum, output cout);
    wire [3:0] carry;
    
    adder FA0 (a[0], b[0], cin, sum[0], carry[0]);
    adder FA1 (a[1], b[1], carry[0], sum[1], carry[1]);
    adder FA2 (a[2], b[2], carry[1], sum[2], carry[2]);
    adder FA3 (a[3], b[3], carry[2], sum[3], cout);

endmodule
