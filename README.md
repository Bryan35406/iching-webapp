# 주역 괘 해석 웹 애플리케이션

전통적인 주역 점괘 해석을 위한 현대적인 웹 애플리케이션입니다.

## 주요 기능

### 🔮 핵심 기능
- **64괘 자동 식별**: 1효~6효 입력으로 64괘 중 해당 괘 자동 식별
- **동효(변효) 처리**: 동효 개수에 따른 전통적인 해석 규칙 완전 구현
- **본괘/지괘/최종해석**: 3단계 해석 시스템
- **자동 괘 뽑기**: 확률 가중치를 적용한 랜덤 괘 생성
- **워드 파일 저장**: 점괘 결과를 전문적인 워드 문서로 저장

### 💻 웹 기능
- **반응형 디자인**: 데스크톱, 태블릿, 모바일 모든 기기 지원
- **직관적인 UI**: 아름답고 사용하기 쉬운 인터페이스
- **실시간 피드백**: 입력값에 따른 즉시 스타일 변화
- **강조 표시**: 중요한 효를 노란 배경으로 강조
- **로딩 애니메이션**: 처리 중 상태를 시각적으로 표시

## 설치 및 실행

### 1. 필수 요구사항
- Python 3.7 이상
- pip (Python 패키지 관리자)

### 2. 설치
```bash
# 저장소 클론 또는 파일 다운로드
git clone [repository-url] 또는 파일 압축 해제

# 프로젝트 디렉토리로 이동
cd 주역

# 필요한 패키지 설치
pip install -r requirements.txt
```

### 3. Gmail 이메일 전송 설정 (선택사항)
이메일 전송 기능을 사용하려면 Gmail 앱 비밀번호가 필요합니다:

1. **Gmail 2단계 인증 활성화**
   - Gmail 계정 설정 > 보안 > 2단계 인증 활성화

2. **앱 비밀번호 생성**
   - Gmail 계정 설정 > 보안 > 앱 비밀번호
   - "앱 선택" > "기타(맞춤 이름)" > "주역 프로그램" 입력
   - 16자리 앱 비밀번호 생성 및 복사

3. **설정 파일 수정**
   ```python
   # email_config.py 파일 수정
   GMAIL_APP_PASSWORD = "생성된_16자리_앱_비밀번호"
   SENDER_EMAIL = "your_gmail@gmail.com"
   RECIPIENT_EMAIL = "braunsoopark@gmail.com"
   ```

### 4. 해석 파일 준비
`해석/` 폴더에 64개 괘별 워드 파일을 준비해야 합니다:
```
해석/
├── 1괘.docx
├── 2괘.docx
├── 3괘.docx
...
└── 64괘.docx
```

**샘플 파일 예시** (`해석/1괘.docx`):
```
건위천 - 창조와 시작의 상징

1효: 잠룡물용(潛龍勿用) - 아직 때가 아니니 잠시 기다려라
2효: 견룡재전(見龍在田) - 덕이 널리 퍼져 좋은 기회가 온다
3효: 군자종일건건(君子終日乾乾) - 하루종일 부지런히 노력하라
4효: 혹약재연(或躍在淵) - 뛸지 말지 신중하게 판단하라
5효: 비룡재천(飛龍在天) - 하늘을 나는 용처럼 큰 성공을 이룬다
6효: 항룡유회(亢龍有悔) - 너무 높이 올라가면 후회가 따른다
```

### 5. 실행
```bash
python app.py
```

웹 브라우저에서 `http://localhost:5001` 접속

## 사용법

### 📝 기본 사용법
1. **질문 입력**: 점을 치고자 하는 질문을 명확하게 입력
2. **효 입력**: 1효부터 6효까지 1(양) 또는 2(음) 입력
3. **동효 선택**: 변하는 효에 동효 체크박스 체크
4. **괘 식별**: "괘 식별하기" 버튼 클릭
5. **결과 확인**: 본괘, 지괘, 최종해석 확인
6. **저장 및 다운로드**: "점괘 결과 저장" 버튼으로 워드 파일 자동 다운로드

### 🎲 자동 괘 뽑기
- "자동 괘 뽑기" 버튼으로 랜덤 괘 생성
- 동효 개수별 확률: 0개(50%), 1개(30%), 2개(15%), 3개(5%)

### 📋 동효별 해석 규칙
- **0개**: 본괘 전체 해석
- **1개**: 본괘 + 동효 강조
- **2개**: 본괘 + 큰 번호 효 강조
- **3개**: 하괘/상괘 중심으로 본괘 또는 지괘
- **4개**: 지괘 + 고정효 중 작은 것 강조
- **5개**: 지괘 + 고정효 강조
- **6개**: 지괘 전체 해석

## 디렉토리 구조

```
주역/
├── app.py              # Flask 웹 서버
├── templates/
│   └── index.html      # 메인 웹 페이지
├── 해석/               # 괘별 해석 워드 파일
│   ├── 1괘.docx
│   ├── 2괘.docx
│   └── ...
├── 출력/               # 저장된 점괘 결과
├── requirements.txt    # Python 의존성
├── README.md          # 이 파일
└── iching_gui.py      # (참고용) 기존 GUI 버전
```

## 기술 스택

- **백엔드**: Flask (Python)
- **프론트엔드**: HTML5, CSS3, JavaScript (ES6+)
- **문서 처리**: python-docx
- **스타일링**: CSS Grid, Flexbox, 그라데이션
- **반응형**: CSS Media Queries

## 특징

### 🎨 디자인
- 현대적이고 세련된 UI/UX
- 그라데이션과 그림자 효과
- 부드러운 애니메이션과 전환
- 직관적인 색상 구분 (본괘: 초록, 지괘: 보라, 최종: 주황)

### ⚡ 성능
- 빠른 괘 식별 알고리즘
- 비동기 처리로 부드러운 사용자 경험
- 최적화된 파일 I/O

### 🔒 안정성
- 입력값 검증 및 오류 처리
- 예외 상황 대응
- 사용자 친화적인 오류 메시지

## 브라우저 호환성

- Chrome (권장)
- Firefox
- Safari
- Edge

## 라이선스

이 프로젝트는 교육 및 개인 사용 목적으로 제공됩니다.

## 문의 및 지원

프로그램 사용 중 문제가 있거나 기능 요청이 있으시면 이슈를 등록해 주세요.

---

**주의사항**: 
- 해석 파일은 사용자가 직접 준비해야 합니다
- 점괘는 참고용이며, 중요한 결정은 신중하게 판단하시기 바랍니다
- 전통적인 주역 해석 규칙을 따르므로 정확한 동효 개수 입력이 중요합니다 

### 💾 파일 저장 방식
- **웹 버전**: 클릭 즉시 브라우저 다운로드 폴더로 자동 다운로드
- **서버 백업**: 동시에 서버의 `출력/` 폴더에도 백업 저장
- **파일명 형식**: `점괘결과_YYYYMMDD_HHMMSS.docx` 

## 업데이트
- 최종 업데이트: 2025-05-28 15:30 (웹 버전 완성) 