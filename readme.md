# FastAPI Parquet 파일 업로드 및 암호화

이 프로젝트는 FastAPI를 사용하여 Parquet 파일을 업로드하고, 해당 파일을 AES128로 암호화하여 서버로 전송하는 예시 코드를 포함하고 있습니다.

## 파일 구성

- `main.py`: FastAPI 애플리케이션 및 파일 업로드 및 암호화 로직이 구현된 코드
- `req_tester.py`: HTTP 클라이언트로 서버에 파일을 업로드하는 코드

## 실행 방법

1. FastAPI 서버 실행:

   ```bash
   uvicorn main:app --reload

2. 테스터 실행:

    ```bash
    python req_tester.py
