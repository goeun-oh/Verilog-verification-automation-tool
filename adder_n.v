module adder_n (input [7:0] a, input [7:0] b, input cin, output [7:0] sum, output cout);
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