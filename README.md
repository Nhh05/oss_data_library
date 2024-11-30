# **PNG to RGB 라이브러리**

PNG 파일을 읽고 픽셀별 RGB 데이터를 추출
파이썬 내장 모듈만을 이용해 구현하기 !

---
## 📌 **만들 기능**
1. PNG 파일의 헤더, 청크별로 데이터 분리, 디코딩
2. 픽셀 데이터(RGB)를 2D 배열로 변환

<hr>
---
---


# **작업 규칙**

## 📌 1. 깃허브 연결
리포지토리를 처음 복사할 때:
```bash
git clone https://github.com/Nhh05/oss_data_library.git
cd oss_data_library
```

---

## 📌 2. 작업 전 항상 pull ! 
작업 시작 전에 항상 최신 코드를 가져옵니다:
```bash
git pull origin main
```

---

## 📌 3. 브랜치 규칙
- **`main` 브랜치**: 직접 수정 금지.
- **개인 브랜치**: `<이름>_<버전>` 형식 사용.
  ```bash
  git branch <브랜치_이름>
  git checkout <브랜치_이름>
  ```
  - 예시: `git branch junseok_1`

---

## 📌 4. 커밋 메시지 규칙
- 형식: `[타입] 작업 내용`
  - `[Feat]`: 새 기능 추가
  - `[Fix]`: 버그 수정
  - `[Docs]`: 문서 수정
  - `[Chore]`: 기타 작업
- **예시**:
  ```bash
  git commit -m "[Feat] Add image processing function"
  ```

---

## 📌 5. 작업 후 업로드
작업 완료 후 변경 사항을 원격 저장소에 업로드:
```bash
git push origin <브랜치_이름>
```
