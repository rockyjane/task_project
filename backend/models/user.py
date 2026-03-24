from sqlalchemy import Column, Integer, String
# Base 是所有資料表的「父類」
from sqlalchemy.orm import declarative_base
# 建立 Base（所有 table 都要繼承）
Base = declarative_base()

class User(Base):
    # 資料表名稱
    __tablename__ = "users"
    # id 主鍵
    id = Column(Integer, primary_key=True, index=True)
    # 使用者名稱
    username = Column(String(50))
    # email
    email = Column(String(100))
    # 密碼
    password = Column(String(200))