from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def home():
    return {"user_id": 1002}


@app.get('/shop')
async def home():
    return {"shop": "商品信息"}


if __name__ == '__main__':
    uvicorn.run("03 fastAPI quickstart:app", port=8080, debug=True, reload=True)