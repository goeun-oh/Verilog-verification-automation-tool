module adder #(parameter WIDTH = 8) (
    input  logic [WIDTH-1:0] a,
    input  logic [WIDTH-1:0] b,
    input  logic             cin,
    output logic [WIDTH-1:0] sum,
    output logic             cout
);
    // 간단 예시: (a + b + cin)
    assign {cout, sum} = a + b + cin;
endmodule
