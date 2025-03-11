from passlib.context import CryptContext

# 创建密码加密上下文
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 对密码进行哈希处理
hashed_password = pwd_context.hash("1245676")
print(hashed_password)
