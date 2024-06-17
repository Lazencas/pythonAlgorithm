import secrets

# 256비트(32바이트) 랜덤 바이트 생성
secret_key = secrets.token_hex(32)
print("Generated secret key:", secret_key)
