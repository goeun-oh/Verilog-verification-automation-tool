
[Start]  
   │  
   ▼  
[Setup Environment]  
   │  
   ▼  
[Generate Verilog Files]  
   ├──> [Generate adder_n.v]  
   ├──> [Generate adder_tb.v]  
   └──> [Push to GitHub]  
   │  
   ▼  
[Generate Input.txt]  
   ├──> [Add Edge Cases]  
   └──> [Push to GitHub]  
   │  
   ▼  
[Run Verilog Simulation]  
   ├──> [Compile Verilog (iverilog)]  
   ├──> [Run Simulation (vvp)]  
   ├──> [Save verilog_output.txt]  
   └──> [Push to GitHub]  
   │  
   ▼  
[Run Python Adder]  
   ├──> [Generate python_output.txt]  
   └──> [Push to GitHub]  
   │  
   ▼  
[Compare Results]  
   ├──> [compare_files.py]  
   ├──> [txt_to_csv.py]  
   ├──> [Save comparison_output.csv]  
   └──> [Push to GitHub]  
   │  
   ▼  
[Calculate Success Rate]  
   ├──> [success_per.py]  
   ├──> [Save success_per.txt]  
   └──> [Push to GitHub]  
   │  
   ▼  
[End]  
