# SQLAlchemy: Python 最主流 ORM（類似用物件操作資料庫）
from sqlalchemy import create_engine
# 建立 DB session（類似「連線實例」）
from sqlalchemy.orm import sessionmaker, Session
import os
# 讀取 .env
from dotenv import load_dotenv

# 載入環境變數（像前端的 .env.local）
load_dotenv()

# 從 .env 拿資料
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# 資料庫連線字串（從環境變數拿 DB 內容）
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# 建立「資料庫引擎」（連線 MySQL）
# 類似：Axios instance / API client
engine = create_engine(DATABASE_URL)

# 建立 Session 工廠（之後每次 request 都會用）
SessionLocal = sessionmaker(
    autocommit=False,  # 不自動 commit
    autoflush=False,   # 不自動 flush
    bind=engine        # 綁定 DB
)

# FastAPI dependency
def get_db():
    # 開一個 DB 連線
    db = SessionLocal()
    try:
        # 把 db 傳給 API 用
        yield db
    finally:
        # 用完一定要關（像 finally cleanup）
        db.close()