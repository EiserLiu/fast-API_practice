from typing import List

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index")
def index(request: Request):
    name: str = "root"
    age: int = 20
    books: List = ["金瓶梅", "聊斋", "剪灯新话", "国色天香"]
    movies = {"chengnian": ["国产", "欧美", "日韩"],
              "qingshaonian": ["黑猫警长", "熊出没", "大头儿子与小头爸爸"]}
    info = {"name": "Eiser", "age": 20, "sex": "男"}
    return templates.TemplateResponse(
        "index.html",  # 模版文件
        {
            "request": request,
            "user": name,
            "age": age,
            "books": books,
            "info": info,
            "movies": movies,
        },  # context上下文对象,一个字典
    )


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)
