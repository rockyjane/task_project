# SQLAlchemy: Python 最主流 ORM（類似用物件操作資料庫）
from sqlalchemy import create_engine
# 建立 DB session（類似「連線實例」）
from sqlalchemy.orm import sessionmaker
import os
# 讀取 .env
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 從 .env 拿資料
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# 資料庫連線字串（超重要）
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"ˇ
)

# 建立「資料庫引擎」
# 類似：Axios instance / API client
engine = create_engine(DATABASE_URL)

# 建立 Session 工廠（之後每次 request 都會用）
SessionLocal = sessionmaker(
    autocommit=False,  # 不自動 commit
    autoflush=False,   # 不自動 flush
    bind=engine        # 綁定 DB
)