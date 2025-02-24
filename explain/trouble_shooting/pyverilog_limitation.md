### **🔧 Verilog 시뮬레이션 Trouble Shooting**  

#### **1️⃣ Verilog 시뮬레이션이 작동하지 않는 문제 발생**  
🔍 **문제:** Python 코드에서 `adder.v`와 `adder_tb.v`를 직접 컴파일하는 것이 아니라, 자체 모듈을 생성하여 실행하려고 시도함.  

💡 **원인 분석:**  
- Pyverilog를 사용하여 Verilog 코드를 실행하려 했으나, **Pyverilog는 정적 분석 도구일 뿐 실제 시뮬레이션을 수행하지 않음**.  
- Verilog 코드를 실행하려면 별도의 **Verilog 시뮬레이터(예: `iverilog` 또는 `ModelSim`)**가 필요함.  

✅ **해결 방법:**  
- 현재 **GitHub Actions에서 Linux 가상 환경을 사용** 중이므로, 해당 환경에서 `iverilog`를 설치하여 Verilog 시뮬레이션을 실행해야 함.  
- `iverilog` 설치 후, 다음 명령어를 실행하여 Verilog 시뮬레이션 수행:  

```bash
- name: Install Icarus Verilog
      run: sudo apt-get update && sudo apt-get install -y iverilog  # iverilog 설치
```
