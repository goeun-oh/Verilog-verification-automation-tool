# 📌 Verilog Verification Automation Tool

![GitHub repo size](https://img.shields.io/github/repo-size/goeun-oh/Verilog-verification-automation-tool)
![GitHub last commit](https://img.shields.io/github/last-commit/goeun-oh/Verilog-verification-automation-tool)
![GitHub contributors](https://img.shields.io/github/contributors/goeun-oh/Verilog-verification-automation-tool)

## 📖 소개
Verilog 기반의 n-bit Full Adder 모듈과 테스트벤치를 자동으로 생성하고 검증하는 Python 기반의 자동화 도구입니다.
Python에서 수행한 Full Adder 연산 결과와 Verilog 시뮬레이션 결과를 비교하여 검증하는 자동화된 검증 시스템을 제공합니다.
본 프로젝트는 설계자가 보다 효율적으로 Verilog 하드웨어 모듈을 개발하고 검증할 수 있도록 지원하는 것을 목표로 합니다.
<br>
<br>

## 🎯 목적
디지털 회로 설계에서 높은 비트수(n-bit) 연산을 포함하는 모듈의 검증 과정은 테스트 케이스를 수동으로 작성해야 하는 번거로움이 존재합니다.
특히 n-bit 연산의 경우 가능한 입력 조합이 기하급수적으로 증가하여, 완전한 검증을 위해서는 방대한 양의 테스트 케이스가 필요합니다.

본 프로젝트는 Verilog 모듈 검증을 자동화하여 이러한 문제를 해결하며, 설계자의 부담을 줄이고 효율적인 하드웨어 검증이 가능하도록 다음과 같은 목표를 가집니다.

✅ 테스트 자동화 – 다양한 n-bit 입력을 자동으로 생성하여, 랜덤 테스트 및 엣지 케이스 검증 수행
✅ Python 기반 설계 자동화 – Verilog 모듈 및 테스트벤치 자동 생성
✅ 교차 검증 시스템 – Python의 연산 결과와 Verilog 시뮬레이션 결과 비교를 통한 자동 검증
✅ CI/CD 기반 자동 검증 환경 구축 – Linux 가상환경 및 GitHub Actions를 활용한 지속적인 검증(CI) 적용

이러한 기능을 통해 설계자의 수작업을 최소화하면서도 신뢰도 높은 검증을 수행할 수 있도록 지원합니다.
<br>
<br>

## 🔧 주요 기능
✅ n-bit Full Adder 설계 자동화
Python을 이용하여 Verilog 기반의 n-bit Full Adder 모듈 및 테스트벤치를 자동으로 생성

✅ Verilog 시뮬레이션 자동화
Linux 환경 및 GitHub Actions를 활용한 Verilog 모듈 자동 검증

✅ 랜덤 및 엣지 케이스 입력 자동 생성
n-bit 연산에서 발생할 수 있는 다양한 입력 조합(랜덤 값, 엣지 케이스)을 자동으로 생성하여 테스트 커버리지 향상

✅ Python-기반 교차 검증
Python에서 연산한 결과와 Verilog 시뮬레이션 결과를 비교하여 정확성을 검증

✅ CI/CD 기반 지속적 검증 지원
GitHub Actions를 활용한 자동 검증 파이프라인 구축

## 🚀 차별점
✔ 완전 자동화된 검증 프로세스
테스트 입력 생성부터 시뮬레이션, 결과 검증까지 모든 과정을 자동화하여 설계자의 검증 부담을 최소화

✔ Python과 Verilog의 교차 검증 시스템
Python에서 직접 Full Adder 연산을 수행하고, 이를 Verilog 시뮬레이션 결과와 비교하여 설계 오류를 신속하게 탐지

✔ CI/CD 적용으로 지속적 검증 가능
GitHub Actions를 활용한 자동화된 검증 환경을 제공하여 코드 변경 시 즉각적인 테스트 및 검증 수행

✔ 확장성 높은 구조
n-bit Full Adder뿐만 아니라, 향후 다양한 디지털 회로 모듈 검증으로 확장 가능

## 📂 파일 구조 및 실행흐름
- **[파일 구조](https://github.com/goeun-oh/Verilog-verification-automation-tool/blob/hotfix_v01/explain/file_structure.md)**
<br>
<br>

## 🏗️ 차별점


## 🏗️ 팀원 역할 분담
**[역할 분담](https://github.com/goeun-oh/Verilog-verification-automation-tool/blob/hotfix_v01/explain/division_role.md)**


<br>


