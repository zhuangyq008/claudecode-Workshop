from fastapi import FastAPI
from routes import app as routes_app
import uvicorn

app = FastAPI()

app.include_router(routes_app)

# 启动服务器
if __name__ == "__main__":
    print("启动请假管理系统...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
