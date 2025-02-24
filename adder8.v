module adderN #(parameter WIDTH = 8) (
    input  [WIDTH-1:0] a,
    input  [WIDTH-1:0] b,
    input              cin,
    output [WIDTH-1:0] sum,
    output             cout
);
    // 내부 carry 연결
    wire [WIDTH-1:0] carry;

    // 첫 번째 비트
    adder FA0 (
        .a(a[0]),
        .b(b[0]),
        .cin(cin),
        .sum(sum[0]),
        .cout(carry[0])
    );

    // 2번째 비트부터 WIDTH-2번째 비트까지
    genvar i;
    generate
        for (i = 1; i < WIDTH-1; i = i + 1) begin : GEN_FA
            adder FA_i (
                .a(a[i]),
                .b(b[i]),
                .cin(carry[i-1]),
                .sum(sum[i]),
                .cout(carry[i])
            );
        end
    endgenerate

    // 마지막 비트
    adder FA_last (
        .a(a[WIDTH-1]),
        .b(b[WIDTH-1]),
        .cin(carry[WIDTH-2]),
        .sum(sum[WIDTH-1]),
        .cout(cout)
    );
endmodule
