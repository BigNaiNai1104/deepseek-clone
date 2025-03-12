# backend/schemas.py
from pydantic import BaseModel

# 定义用户创建模式
class UserCreate(BaseModel):
    username: str
    password: str  # 你可以添加更多字段，如 email 等

# 你的 Item 模式
class ItemCreate(BaseModel):
    name: str
    description: str

class Item(ItemCreate):
    id: int

    class Config:
        orm_mode = True
