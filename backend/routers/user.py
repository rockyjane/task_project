# FastAPI router（就像前端的 route module / API module）
from fastapi import APIRouter, Depends
# SQLAlchemy 的 session（用來操作資料庫）
from sqlalchemy.orm import Session
# 引入 DB 連線（dependency injection）
from database import get_db
# 引入 ORM(資料庫操作工具) model（資料表）
from models.user import User
# 引入 schema（資料驗證用）
from schemas.user import UserCreate
# 密碼加密工具（套件）
from passlib.context import CryptContext

# 建立 router（像 Vue Router module）
router = APIRouter()
# router = APIRouter(
#     prefix="/users",   # API 路徑前綴
#     tags=["users"]     # Swagger 分類
# )

# 建立密碼加密設定
"""
bcrypt 演算法(目前主流安全方案)
特性：
不可逆（hash ≠ encrypt）
每次 hash 都不同（有 salt）
防止資料庫外洩
"""
pwd_context = CryptContext(
    schemes=["bcrypt"],   # 使用 bcrypt 演算法
    deprecated="auto"
)

# POST /register API
@router.post("/register")
def register(
    user: UserCreate,             # request body（自動驗證）
    db: Session = Depends(get_db) # 注入 DB（SQL ORM 化接著注入）
):
    """
    使用者註冊 API

    流程：
    1. 接收前端資料
    2. Pydantic 自動驗證
    3. 密碼加密
    4. 寫入資料庫
    """
    # 密碼加密
    hashed_password = pwd_context.hash(user.password)

    # 建立一個 User 物件（還沒進 DB）
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
    )
    # 加入 DB session（像 queue or 還沒 commit）
    db.add(new_user)
    # 真正寫入 DB（= SQL INSERT or commit）
    db.commit()
    # refresh（拿回 DB 最新資料，例如 id）
    db.refresh(new_user)
    # 回傳結果
    return {"message": "user created"}