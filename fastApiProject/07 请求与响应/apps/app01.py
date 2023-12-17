from fastapi import APIRouter


app01 = APIRouter()


# @app.get('/user/{user_Id}')
# async def get_user(user_id: int):
#     return {"user_id": user_id}
#
#
# @app.get('/articles/{article_Id}')
# async def get_user(article_id: int):
#     return {"article_id": article_id}


# 顺序影响路径
@app.get('/user/me')
async def read_user_me():
    return {"user_id": "the current user"}


@app.get('/user/{username}')
async def read_user(username: str):
    return {"user_name": username}

