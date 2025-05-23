## 🔍 Random Testing의 한계와 Edge Case 고려 과정

### 🛠 문제
가산기(Adder)의 동작을 검증하기 위해 입력 값을 무작위로 테스트하는 자동화를 구현하였다. 하지만, 무작위 테스트 방식으로 인해 대부분 일반적인 케이스만 검증되었다.

### 📌 원인 분석
- 무작위 테스트만으로는 중요한 Edge Case를 충분히 검증하지 못함.
- 따라서, Edge Case를 자동으로 탐색하는 방식으로 접근할 필요가 있음.

### ✅ 해결 방법
1. **비트 폭(bit_width)에 따른 Edge Case 자동 생성**
   - `number.txt`에서 비트 폭을 읽어와 이에 맞춰 테스트 데이터를 생성하도록 코드 수정.
   - 다양한 환경에서도 동일한 검증이 가능하도록 유연성 확보.

2. **오버플로우(Overflow) 감지 로직 추가**
   - `check_overflow(a, b, bit_width)` 함수를 추가하여 최대값을 초과하는 경우 감지.

3. **Edge Case 자동 탐색 및 `input.txt`에 추가**
   - 최소값, 최대값, 최대값-1, 연속된 값, 중간값+1, 중간값+2 등의 Edge Case를 자동 생성하여 테스트.
   - 각 케이스를 이진수 변환 후 `input.txt`에 저장하도록 구현.

4. **테스트 자동화 및 기록 방식 개선**
   - `input.txt`를 덮어쓰지 않고, 기존 데이터에 Edge Case 테스트 결과를 계속 추가하도록 기록 방식 개선.

### 🎯 결과
- Edge Case 자동 탐색을 통해 테스트 정확도 향상.
- 예상치 못한 오버플로우 및 경계값 오류를 사전에 탐지 가능.
