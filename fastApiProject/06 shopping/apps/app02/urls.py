from fastapi import APIRouter
import uvicorn

user = APIRouter()


@user.post('/login')
async def user_login():
    return {"user": "login"}


@user.post('/reg')
async def user_reg():
    return {"user": "reg"}


if __name__ == '__main__':
    uvicorn.run("03 fastAPI quickstart:app", port=8080, debug=True, reload=True)