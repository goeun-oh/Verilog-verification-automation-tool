[Start]  
   │  
   ▼  
[Generate Verilog Files]       
   ├──> [Generate adder.v]  
   ├──> [Run generate_vfile.py]  
   ├──> [Run generate_tb.py]       
   ▼  
[Generate Input.txt]   
   ├──> [Run generate_input.py]  
   ├──> [Run edge_case.py]  
   ├──> [Generate Input.txt]   
   ▼  
[Run Verilog Simulation]    
   ├──> [Compile Verilog (iverilog)]  
   ├──> [Run Simulation (vvp)]  
   ├──> [Generate verilog_output.txt]    
   ▼  
[Run Python Adder]  
   │  
   ├──> [Run python_adder.py]  
   ├──> [Generate python_output.txt]  
   │  
   ▼  
[Compare Results]  
   │  
   ├──> [Run compare_files.py]  
   ├──> [Run txt_to_csv.py]  
   ├──> [Save comparison_output.csv]  
   │  
   ▼  
[Calculate Success Rate]  
   │  
   ├──> [Run success_per.py]  
   ├──> [Generate success_per.txt]  
   │  
   ▼  
[End]  
