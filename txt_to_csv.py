import csv
import datetime, timezone
from zoneinfo import ZoneInfo

# 파일 경로
python_file = "python_output.txt"
verilog_file = "verilog_output.txt"
output_csv = "comparison_output.csv"

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

# CSV 파일 작성
with open(output_csv, "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    # 헤더 작성
    csv_writer.writerow(["a", "b", "cin", "추출시간", "Python_sum", "Python_cout", "Verilog_sum", "Verilog_cout", "일치여부"])

    # 데이터 비교 및 기록
    now_utc = datetime.now(timezone.utc)
    now_kst = now_utc.astimezone(ZoneInfo("Asia/Seoul"))
    now = now_kst.strftime("%Y-%m-%d %H:%M:%S")
    for (a, b, cin, py_sum, py_cout), (a, b, cin, verilog_sum, verilog_cout) in zip(python_results, verilog_results):
        match = "O" if (py_sum == verilog_sum and py_cout == verilog_cout) else "X"
        csv_writer.writerow([a, b, cin, now, py_sum, py_cout, verilog_sum, verilog_cout, match])

print(f"CSV 파일 생성 완료: {output_csv}")
