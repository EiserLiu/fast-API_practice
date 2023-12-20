import time

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

app = FastAPI()

origins = [
    "https://localhost:63342"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.middleware("http")
async def m2(request: Request, call_next):
    # 请求代码块
    print("m2 request")
    response = await call_next(request)
    # 响应代码块
    response.headers["author"] = "Eiser"
    print("m2 response")
    return response


@app.middleware("http")
async def m1(request: Request, call_next):
    # 请求代码块
    print("m1 request")
    start = time.time()
    if request.url.path in ["/user"]:
        return Response(content="visit forbidden")
    response = await call_next(request)
    # if request.client.host in ["127.0.0.1"]:
    #     return Response(content="visit forbidden")

    # 响应代码块
    print("m1 response")
    end = time.time()
    t = response.headers["ProcessTimer"] = str(end - start)
    print(t)
    return response


@app.get("/user")
def get_user():
    time.sleep(3)
    print("get_user函数执行")
    return {
        "user": "current user"
    }


@app.get("/item/{item_id}")
def get_user(item_id: int):
    time.sleep(2)
    print("get_itme函数执行")
    return {
        "item_id": item_id
    }


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8080, reload=True, workers=1)
