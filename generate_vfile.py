def gen_v(v, bit_width):
    with open(v, "w") as v:
        v.write(f"module adder_n (input [{bit_width}:0] a, input [{bit_width}:0] b, input cin, output [{bit_width}:0] sum, output cout);\n")
        v.write(f"    wire [{bit_width}:0] carry;\n\n")
        v.write(f"    adder FA0 (a[0], b[0], cin, sum[0], carry[0]);\n")
        for i in range(bit_width-2):
            v.write(f"    adder FA{i+1} (a[{i+1}], b[{i+1}], carry[{i}], sum[{i+1}], carry[{i+1}]);\n")
        v.write(f"    adder FA{bit_width-1} (a[{bit_width-1}], b[{bit_width-1}], carry[{bit_width-2}], sum[{bit_width-1}], cout);\n")
        v.write("endmodule")
        
        
def fetch_num():
    with open("number.txt","r") as f:
        bit_width=int(f.read().strip())
    return bit_width
    
    
    
bit_width=fetch_num()
gen_v("adder_n.v", bit_width)
