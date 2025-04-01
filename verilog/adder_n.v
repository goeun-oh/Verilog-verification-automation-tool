module adder_n (input [15:0] a, input [15:0] b, input cin, output [15:0] sum, output cout);
    wire [15:0] carry;

    adder FA0 (a[0], b[0], cin, sum[0], carry[0]);
    adder FA1 (a[1], b[1], carry[0], sum[1], carry[1]);
    adder FA2 (a[2], b[2], carry[1], sum[2], carry[2]);
    adder FA3 (a[3], b[3], carry[2], sum[3], carry[3]);
    adder FA4 (a[4], b[4], carry[3], sum[4], carry[4]);
    adder FA5 (a[5], b[5], carry[4], sum[5], carry[5]);
    adder FA6 (a[6], b[6], carry[5], sum[6], carry[6]);
    adder FA7 (a[7], b[7], carry[6], sum[7], carry[7]);
    adder FA8 (a[8], b[8], carry[7], sum[8], carry[8]);
    adder FA9 (a[9], b[9], carry[8], sum[9], carry[9]);
    adder FA10 (a[10], b[10], carry[9], sum[10], carry[10]);
    adder FA11 (a[11], b[11], carry[10], sum[11], carry[11]);
    adder FA12 (a[12], b[12], carry[11], sum[12], carry[12]);
    adder FA13 (a[13], b[13], carry[12], sum[13], carry[13]);
    adder FA14 (a[14], b[14], carry[13], sum[14], carry[14]);
    adder FA15 (a[15], b[15], carry[14], sum[15], cout);
endmodule