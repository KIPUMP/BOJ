import jwt
import csv
import time
import base64

# 비밀 키 (Base64 인코딩된 비밀 키)
secret_key = base64.b64encode(b'7Leo7JeF7L2U7Iqk7ZmU7J207YyF7ZW064u56rWQ7Jyh6rO87KCV7J2E64Gd64K06rOg64KY66m06ryt7Leo7JeF7ZWY7Iuk7IiY7J6I7J2E6rKB64uI64ukLg==').decode('utf-8')

# JWT 생성 함수
def create_jwt(user_id, role):
    payload = {
        "sub": user_id,  # 사용자 식별자값(ID)
        "auth": role,    # 사용자 권한
        "exp": time.time() + (60 * 60 * 24 * 7)  # 7일 후 만료
    }
    token = jwt.encode(payload, base64.b64decode(secret_key), algorithm="HS256")
    return token

# 10,000개의 JWT 생성 및 CSV 파일로 저장
with open('jwt_tokens.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["userId", "jwt_token"])
    for i in range(1, 10001):
        user_id = f"user_{i}"
        role = "USER"  # 사용자 권한 설정, 예: 일반 사용자
        jwt_token = create_jwt(user_id, role)
        writer.writerow([user_id, jwt_token])

print("10,000개의 JWT가 'jwt_tokens.csv' 파일에 저장되었습니다.")