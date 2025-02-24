module adder (a,b,cin,sum,cout);

    input a, b, cin;
    output sum, cout;
    wire s1, c1, c2;
     
    xor  G1(s1, a, b);
    and  G2(c1, a, b);
    and  G3(c2, cin, s1);
    xor  G4(sum, s1, cin);
    or  G5(cout, c1, c2);
     
endmodule
