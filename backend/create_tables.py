from database import engine
from models.user import Base

# 建立所有 Base 底下的 table
Base.metadata.create_all(bind=engine)

print("tables created")