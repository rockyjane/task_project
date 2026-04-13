from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# DB dependency
from database import get_db
# 資料表 model（對應 MySQL table）
from models.user import User
# request schema（驗證用）
from schemas.user import UserCreate

# 建立 router（像 Vue Router module）
router = APIRouter()

# POST /register API
@router.post("/register")
def register(
    user: UserCreate,             # request body（自動驗證）
    db: Session = Depends(get_db) # 注入 DB（很重要）
):
    # 建立一個 User 物件（還沒進 DB）
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
    )
    # 加進 session（還沒 commit）
    db.add(new_user)
    # 寫入 DB（= SQL INSERT）
    db.commit()
    # 重新讀取（拿 ID 等資料）
    db.refresh(new_user)
    # 回傳結果
    return {"message": "user created"}