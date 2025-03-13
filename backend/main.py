from fastapi import FastAPI, HTTPException, Depends, Form, Header
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend import models, schemas  # 绝对导入
from pydantic import BaseModel

# 数据库连接配置
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:021104@localhost:3306/deepseek_clone"

# 创建数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20)

# 设置 SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 确保数据库表被正确创建（建议移到 models.py）
models.Base.metadata.create_all(bind=engine)

# 依赖项：获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 创建 FastAPI 实例
app = FastAPI()

# CORS 配置，允许前端访问
origins = ["http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 添加根路径
@app.get("/")
async def root():
    return {"message": "Welcome to DeepSeek Clone API!"}

# ✅ 用户注册接口
@app.post("/register")
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = models.User(username=user.username, password=user.password, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

# ✅ 登录接口
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.password != password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"success": True, "token": user.username}  # 临时用 username 作为 token

# ✅ 获取用户资料接口
@app.get("/profile")
async def get_profile(authorization: str = Header(None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing token")

    token = authorization.split(" ")[1]  # 解析 token，暂时把 username 当 token
    user = db.query(models.User).filter(models.User.username == token).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "username": user.username,
        "email": user.email
    }
