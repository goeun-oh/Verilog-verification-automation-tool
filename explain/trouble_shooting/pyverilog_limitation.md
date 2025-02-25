### **🔧 Verilog 시뮬레이션 Trouble Shooting**  

#### **Verilog 시뮬레이션이 작동하지 않는 문제 발생**  
🔍 **문제:**   
설계한 가산기 모듈(`adder.v`, `adder_tb.v`) 컴파일을 위해 관련 Python library(`Pyverilog`) 를 import하여 python 파일 내부에서 컴파일을 시도함

💡 **원인 분석:**  
- **Pyverilog는 정적 분석 도구일 뿐 실제 시뮬레이션을 수행하지 않음**.  
- Verilog 코드를 실행하려면 별도의 **Verilog 시뮬레이터(예: `iverilog` 또는 `ModelSim`)**가 필요함을 발견  

✅ **해결 방법:**  
- 현재 **GitHub Actions에서 Linux 가상 환경을 사용** 중이므로, 해당 환경에서 `iverilog`를 설치 후 linux 환경에서 Verilog 시뮬레이션 수행 
- `iverilog` 설치 후, 다음 명령어를 실행하여 Verilog 시뮬레이션 수행:  

```yaml
- name: Install Icarus Verilog
    run: sudo apt-get update && sudo apt-get install -y iverilog  # iverilog 설치

- name:  Run Verilog
    run: iverilog -o adder_sim verilog/adder.v verilog/adder_n.v verilog/adder_tb.v  # Verilog 컴파일
```

### 🎯 **결과**  
✅ **Verilog 시뮬레이션 정상 동작 확인**  
- `iverilog` 설치 후 linux 환경에서 iverilog를 실행하여 `adder_tb.v`와 `adder.v`를 정상적으로 컴파일
  
✅ **GitHub Actions에서 자동 실행 가능**  
- GitHub Actions CI/CD 파이프라인에서 Verilog 시뮬레이션이 자동으로 실행되며, 빌드 프로세스가 정상적으로 동작함.  
- 향후 Testbench 검증 과정에서 Verilog 테스트 결과를 로그로 확인 가능.  
