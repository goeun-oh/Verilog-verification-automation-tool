# txt_to_csv.py - 결과 종합 csv

## 📖 result_verification branch
python_output.txt과 verilog_output.txt에서 input data와 각각의 결과 값을 가져와 합친 내용을 csv 파일로 만드는 python파일
a,	b,	cin,	추출시간,	Python_sum,	Python_cout,	Verilog_sum,	Verilog_cout,	일치여부의 형태

## 🚀 주요 기능

### ✅ 1. 파일 읽기 
이 스크립트는 **Python에서 txt파일을 읽기**하고, 결과를 `csv`에 저장한다.  

📌 **기능 상세**
- python_file에서 a, b, cin, Python_sum, Python_cout, Verilog_sum, Verilog_cout을 읽어온다.
- " -> sum: "을 기준으로 분리한다.
- 왼쪽의 값을 띄어쓰기로 분리하여 a, b, cin을 얻는다.
- 오른쪽의 결과를 ", cout: " 기준으로 분리하여 sum과 cout을 구한다.
- Python의 결과와 Verilog의 결과를 모두 돌려 각각의 값을 얻는다.

### ✅ 2. 스크립트 실행 시간 가져오기
이 스크립트는 결과 값을 비교한 시간을 가져온다. 추출시간에 한국 시간으로 입력한다.

📌 **기능 상세**
- import datetime과 from datetime import timezon의 차이점
    
    1. import datetime은 모듈 전체를 가져와서 timezone 객체는 datetime 모율의 하위 모듈인 datetime.timezon으로 접근한다.
    2. from datetime import timezone은 datetime 모듈에서 timezone 객체만을 직접 가져와서 timezone으로 바로 사용 가능하다.
 
- utc kst 시간으로 변환
    
    1. 시간대 정보가 없는 객체에 대해 astimezone을 쓸 수 없으므로
       현재 시간을 가져와서
       from datetime import datetime, timezone
       from zoneinfo import ZoneInfo
       now_utc = datetime.now(timezone.utc)
    
    2. zoneinfo 모듈을 가져와서 Asia/Seoul의 정보를 가져와 시간대 변환
       now_kst = now_utc.astimezone(ZoneInfo("Asia/Seoul"))
       now = now_kst.strftime("%Y-%m-%d %H:%M:%S")

### ✅ 3. 일치 여부 확인
py_sum과 verilog_sum 그리고 py_cout과 verilog_cout을 비교하여 일치 여부를 확인한다.

📌 **기능 상세**
- py_sum == verilog_sum and py_cout == verilog_cout을 확인 하여 일치여부 항목에 일치 하면 O, 불일치 하면 X를 출력한다.

### ✅ 4. csv 기록
헤더를 만들고 일정 시간마다 추가로 갱신한다.

📌 **기능 상세**
  - with open(output_csv, "w", newline="") as csvfile:
    
    1. 덮어쓰는 방식으로 csv 파일이 생성되므로 csv 파일에 추가되는 방식으로 변경하낟.
       
    2. csv 파일 작성 혹은 존재 확인
       file_exists = os.path.isfile(output_csv)

    3. w를 a로 바꿔 데이터가 추가되는 방식으로 바꾼다.
       with open(output_csv, "a", newline="") as csvfile: 

    4. 파일이 없으면 헤더 작성한다.
       if not file_exists:
         csv_writer.writerow(["a", "b", "cin", "추출시간", "Python_sum", "Python_cout", "Verilog_sum", "Verilog_cout", "일치여부"])

  
    
    
