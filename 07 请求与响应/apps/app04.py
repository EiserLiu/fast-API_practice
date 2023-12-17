from fastapi import APIRouter, Form

app04 = APIRouter()


@app04.post("/regin")
async def reg(username: str = Form(), password: str = Form()):
    print(f"username:{username},password:{password}")
    # 注册,数据库添加操作
    return {
        "username": username
    }
