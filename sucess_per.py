import csv

# CSV 파일 경로
csv_file_path = 'comparison_output.csv'  # CSV 파일의 실제 경로로 변경해주세요

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
    print(f"성공률: {success_rate:.2f}%")
else:
    print("데이터가 없습니다.")
