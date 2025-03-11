from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from passlib.context import CryptContext
import jwt
import datetime
from fastapi.middleware.cors import CORSMiddleware

# FastAPI 应用实例
app = FastAPI()

# 允许跨域请求（前端 Vue 需要）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有 Headers
)

# 数据库连接
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:021104@localhost:3306/deepseek_clone"  # 修改为 MySQL 连接
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建数据库模型基类
Base = declarative_base()

# 密码加密
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT 配置
SECRET_KEY = "secret-key"  # 请更换为更强的密钥
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 定义用户表
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True)  # 添加 email 字段

# 创建数据库
Base.metadata.create_all(bind=engine)

# 获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 依赖项 - 获取当前用户
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise credentials_exception
        return user
    except jwt.PyJWTError:
        raise credentials_exception

# Pydantic 模型
class UserCreate(BaseModel):
    username: str
    password: str
    email: str  # 添加 email 字段

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str  # 添加 email 字段

    class Config:
        orm_mode = True

# 注册用户
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # 检查用户名是否已存在
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # 检查邮箱是否已存在
    db_email = db.query(User).filter(User.email == user.email).first()
    if db_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 创建用户
    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=user.username, password=hashed_password, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 登录，返回 JWT Token
@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode({"sub": user.username, "exp": datetime.datetime.utcnow() + access_token_expires},
                              SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": access_token, "token_type": "bearer"}

# 更新用户信息（需要身份验证）
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # 只允许本人或管理员修改
    if db_user.username != current_user.username:
        raise HTTPException(status_code=403, detail="Not allowed to update this user")

    db_user.username = user.username
    db_user.password = pwd_context.hash(user.password)
    db_user.email = user.email  # 更新 email
    db.commit()
    db.refresh(db_user)
    return db_user

# 删除用户（需要身份验证）
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # 只允许本人或管理员删除
    if db_user.username != current_user.username:
        raise HTTPException(status_code=403, detail="Not allowed to delete this user")

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}

# 测试 API
@app.get("/")
def read_root():
    return {"message": "Welcome to the DeepSeek Clone API"}
