import os
import csv
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# 파일 경로
script_dir = os.path.dirname(os.path.abspath(__file__))
python_file = os.path.join(script_dir, "python_output.txt")
verilog_file = os.path.join(script_dir,"verilog_output.txt")
output_csv = os.path.join(script_dir, "comparison_output.csv")  # ✅ 절대 경로로 변경

# 파일 읽기 함수
def read_results(filename):
    results = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(" -> sum: ")
            if len(parts) != 2:
                continue  # 잘못된 형식 건너뛰기
            inputs, outputs = parts
            a, b, cin = inputs.split()
            sum_val, cout_val = outputs.split(", cout: ")
            results.append((a, b, cin, sum_val, cout_val))
    return results

# 파일에서 데이터 읽기
python_results = read_results(python_file)
verilog_results = read_results(verilog_file)

# CSV 파일 작성 (추가 모드)
file_exists = os.path.isfile(output_csv)

with open(output_csv, "a", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # 파일이 존재하지 않으면 헤더 작성
    if not file_exists:
        csv_writer.writerow(["a", "b", "cin", "추출시간", "Python_sum", "Python_cout", "Verilog_sum", "Verilog_cout", "일치여부"])

    # 데이터 비교 및 기록
    now_utc = datetime.now(timezone.utc)
    now_kst = now_utc.astimezone(ZoneInfo("Asia/Seoul"))
    now = now_kst.strftime("%Y-%m-%d %H:%M:%S")
    for (a, b, cin, py_sum, py_cout), (a, b, cin, verilog_sum, verilog_cout) in zip(python_results, verilog_results):
        match = "O" if (py_sum == verilog_sum and py_cout == verilog_cout) else "X"
        csv_writer.writerow([a, b, cin, now, py_sum, py_cout, verilog_sum, verilog_cout, match])

print(f"CSV 파일 업데이트 완료: {output_csv}")
