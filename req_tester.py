import http.client
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


def encrypt_aes128(plaintext):
    # AES 암호화에 사용되는 키와 IV (반드시 16바이트여야 합니다.)
    secret_key = b'mysecretkey12345'
    iv = b'initialvector123'

    # AES 암호화
    cipher = AES.new(secret_key, AES.MODE_CBC, iv)
    encrypted_bytes = cipher.encrypt(pad(plaintext, AES.block_size))
    return base64.b64encode(encrypted_bytes)


def upload_parquet_file(url, file_path):
    # 파일 열기
    file_data = open(file_path, 'rb').read()
    print(f"Content: {file_data}")

    # 파일 내용을 AES로 암호화
    encrypted_data = encrypt_aes128(file_data)
    # 암호화 후 내용 출력
    print(f"Encrypted content: {encrypted_data}")

    # 요청 헤더 설정
    headers = {
        'Content-Type': 'application/vnd.apache.parquet'
    }

    # 연결 및 요청 보내기
    connection = http.client.HTTPConnection('127.0.0.1', 8000)
    connection.request('POST', '/upload-parquet/', encrypted_data, headers)

    # 응답 받기
    response = connection.getresponse()

    # 응답 출력
    print(f'Status Code: {response.status}')
    print(response.read().decode())


if __name__ == "__main__":
    upload_parquet_file('http://127.0.0.1:8000/upload-parquet/',
                        'C:\\Users\\ninec\\Downloads\\BSMSSM-91\\battery-charge-info-240215.parquet')
