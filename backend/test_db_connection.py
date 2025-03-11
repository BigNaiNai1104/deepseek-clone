from sqlalchemy import create_engine

# MySQL 数据库连接字符串
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:021104@localhost:3306/deepseek_clone"

# 创建数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 测试数据库连接
try:
    with engine.connect() as connection:
        print("MySQL connection successful!")
except Exception as e:
    print("Error connecting to MySQL:", e)
