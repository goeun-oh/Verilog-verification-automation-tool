def gen_tb(tb, bit_width):
    instance_lines = ["adder uut (\n", "    .a(a), .b(b), .cin(cin), .sum(sum), .cout(cout)\n", " );" ]
    file_lines=["    integer fd_in, fd_out;\n", "    integer scan_result;\n", "\n"]
    initial_lines=["    initial begin\n\n", '        fd_in = $fopen("input.txt", "r");\n','        fd_out = $fopen("verilog_output.txt", "w")\n\n', ]
    is_fdin=["        if (fd_in == 0) begin\n", '            $display("Error: input.txt file not found.");\n', "            $finish;\n", "        end\n\n"]
    is_input_end=["        while (!$feof(fd_in)) begin\n", '            scan_result = $fscanf(fd_in, "%b %b %b\n", a, b, cin);\n', "            #10;\n\n", '            $fwrite(fd_out, "%b %b %b -> sum: %b, cout: %b\n", a, b, cin, sum, cout);\n', '        end\n\n']
    file_close=["        $fclose(fd_in);\n", "        $fclose(fd_out);\n", "        $finish;\n"]
    line_end=["    end\n", "endmodule"]
    
    with open(tb, "w") as tb:
        tb.write("module adder_tb;\n")
        tb.write(f"reg [{bit_width}:0] a, b;\n")
        tb.write(f"reg cin;")
        tb.write(f"    wire [{bit_width}:0] sum;")
        tb.write(f"cout;")
        tb.writelines(instance_lines)
        tb.writelines(file_lines)
        tb.writelines(initial_lines)
        tb.writelines(is_fdin)
        tb.writelines(is_input_end)
        tb.writelines(file_close)
        tb.writelines(line_end)
        
        
        

        
def fetch_num():
    with open("","r") as f:
        bit_width=int(f.read().strip())
    return bit_width
    
    
    
bit_width = fetch_num()
gen_tb("adder_tb.v", bit_width)
