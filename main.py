from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

app = FastAPI()

# 암호화키
secret_key = b'mysecretkey12345'
iv = b'initialvector123'


def decrypt_aes128(ciphertext):
    cipher = AES.new(secret_key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(base64.b64decode(ciphertext)), AES.block_size)
    return decrypted_bytes


# Parquet content-type을 가진 파일만 허용하는 업로드 라우트
@app.post("/upload-parquet/")
async def upload_parquet_file(request: Request):
    content_type = request.headers.get("Content-Type")
    if not content_type or content_type != "application/vnd.apache.parquet":
        raise HTTPException(status_code=400,
                            detail="Only Parquet files are allowed with content-type application/vnd.apache.parquet")

    # request body 및 headers를 확인하여 출력
    encrypted_body = await request.body()
    headers = dict(request.headers)
    print(f"Received encrypted request body: {encrypted_body}")
    print(f"Received request headers: {headers}")

    # AES128 복호화
    decrypted_body = decrypt_aes128(encrypted_body)
    print(f"Decrypted request body: {decrypted_body}")

    # TODO: S3 Handling 추가

    return JSONResponse(content={"message": "Parquet file uploaded successfully"})
