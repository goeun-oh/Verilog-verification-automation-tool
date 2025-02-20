def compare_files(python_output_file, verilog_output_file):
    """ Python과 Verilog의 실행 결과 파일을 비교하는 함수 """
    print(f"🔍 파일 비교 중: {python_output_file} vs {verilog_output_file}")

    # 파일 읽기
    with open(python_output_file, "r") as py_file, open(verilog_output_file, "r") as v_file:
        python_lines = py_file.readlines()
        verilog_lines = v_file.readlines()

    # 줄 수가 다르면 에러 처리
    if len(python_lines) != len(verilog_lines):
        print("⚠️ 경고: Python과 Verilog 결과 파일의 줄 수가 다릅니다!")
        print(f"Python 파일 줄 수: {len(python_lines)}, Verilog 파일 줄 수: {len(verilog_lines)}")

    # 결과 비교
    all_match = True
    for line_num, (py_line, v_line) in enumerate(zip(python_lines, verilog_lines), start=1):
        py_line = py_line.strip()
        v_line = v_line.strip()

        if py_line != v_line:
            print(f"❌ 불일치 (Line {line_num}):")
            print(f"   Python: {py_line}")
            print(f"   Verilog: {v_line}")
            all_match = False
        else:
            print(f"✅ 일치 (Line {line_num}): {py_line}")

    # 최종 결과 출력
    if all_match:
        print("\n🎯 모든 결과가 완벽하게 일치합니다!")

compare_files("python_output.txt", "verilog_output.txt")
