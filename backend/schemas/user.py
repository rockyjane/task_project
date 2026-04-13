from pydantic import BaseModel

# 這個就像前端的「表單格式定義 + 驗證」
class UserCreate(BaseModel):
    # 必填 username（字串）
    username: str
    # 必填 email（字串）
    email: str
    # 必填 password（字串）
    password: str