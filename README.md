---
## 🚀 주요 기능
  - generate_input.py	: 랜덤 8비트 입력값(A, B, Cin) 생성 및 저장 (input.txt)
---
### ✅ 1. Python으로 입력 데이터 생성(generate_input.py)

📌 **기능 상세**

  - with open("대상파일", "w"(쓰기) or "r"(읽기)) as file
    1. file을 open하고 close()안하는 것을 방지하기 위해 사용
    2. open 구문 종료시 close()가 동작
    3. random.randint(0,1)로 생성된 값 txt 파일에 저장하기 위해 사용
  
### ✅ 2. Python output과 Verilog output 비교 후 일치 여부 csv 형식으로 기록 (txt_to_csv.py)

📌 **기능 상세**

  - import datetime과 from datetime import timezon의 차이점
    1. import datetime은 모듈 전체를 가져와서 timezone 객체는 datetime 모율의 하위 모듈인 datetime.timezon으로         접근하게 됨
    2. from datetime import timezone은 datetime 모듈에서 timezone 객체만을 직접 가져와서 timezone으로 바로 사         용 가능
   
  - with open(output_csv, "w", newline="") as csvfile: 수정
    1. 위의 방식으로 하면 csv 파일에 추가되는 방식이 아닌 덮어쓰는 방식으로 csv 파일이 생성 됨
    2. file_exists = os.path.isfile(output_csv)러 csv 파일 작성 혹은 존재 확인
       with open(output_csv, "a", newline="") as csvfile: w를 a로 바꿔 데이터가 추가되는 방식으로 바뀜
       if not file_exists:
        csv_writer.writerow(["a", "b", "cin", "추출시간", "Python_sum", "Python_cout", "Verilog_sum", "Verilog_cout", "일치여부"])
       파일이 없으면 헤더 작성

  - utc kst 시간으로 변환
    시간대 정보가 없는 객체에 대해 astimezone을 쓸 수 없으므로
    현재 시간을 가져와서
    from datetime import datetime, timezone
    from zoneinfo import ZoneInfo
    now_utc = datetime.now(timezone.utc)
    
    zoneinfo 모듈을 가져와서 Asia/Seoul의 정보를 가져와 시간대 변환
    now_kst = now_utc.astimezone(ZoneInfo("Asia/Seoul"))
    now = now_kst.strftime("%Y-%m-%d %H:%M:%S")
    
    
