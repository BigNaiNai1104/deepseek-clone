from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from backend import models, schemas  # 绝对导入
from contextlib import asynccontextmanager
from pydantic import BaseModel

# 数据库连接和会话配置
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# 创建数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基础类
Base = declarative_base()

# 依赖：获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 定义登录请求的 Pydantic 模式（如果没有在 schemas 中定义，可以在这里定义）
class LoginRequest(BaseModel):
    username: str
    password: str

# 使用 lifespan 事件处理器代替 on_event
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时创建所有表（如果不存在）
    Base.metadata.create_all(bind=engine)
    yield
    # 关闭时执行的代码（如有需要）
    pass

# 设置 FastAPI 应用实例
app = FastAPI(lifespan=lifespan)

# 设置 CORS 中间件，以允许跨域请求
origins = [
    "http://localhost:8080",  # 前端地址
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许的源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)

# 用户注册接口
@app.post("/register")
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 检查用户名是否已存在
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # 创建并保存新用户
    new_user = models.User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 用户登录接口
@app.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    # 根据用户名查询用户
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 检查密码（这里为简单示例，实际项目中建议使用加密）
    if user.password != request.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # 登录成功后返回一个示例 token（后续可集成 JWT 等机制）
    return {"success": True, "token": "dummy-token"}
