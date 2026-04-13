from fastapi import FastAPI
from routers.user import router as user_router # 匯入 user router

app = FastAPI() # 建立 app（像 Vue new Vue()）
app.include_router(user_router) # 掛上 router（像 use router）

@app.get("/")
def root():
    return {"message": "Task API running"}