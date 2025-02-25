import csv
import os
# CSV 파일 경로
csv_file_path = 'comparison_output.csv'

# 성공 횟수와 전체 횟수를 저장할 변수 초기화
success_count = 0
total_count = 0

# CSV 파일 읽기
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # 각 행을 순회
    for row in csv_reader:
        # 마지막 열의 값 확인
        result = row[-1]
        
        # 전체 횟수 증가
        total_count += 1
        
        # 성공 여부 확인
        if result == 'O':
            success_count += 1

# 성공률 계산
if total_count > 0:
    success_rate = (success_count / total_count) * 100
    result_message = f"성공률: {success_rate:.2f}%"
else:
    result_message = "데이터가 없습니다."

# 결과를 TXT 파일로 저장
with open("success_per.txt", 'w') as file:
    file.write(result_message)
