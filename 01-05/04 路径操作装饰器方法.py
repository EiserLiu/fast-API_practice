from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/get')
async def get_test():
    return {"method": "get方法"}


@app.post('/post')
async def post_test():
    return {"method": "post方法"}

@app.put('/put')
async def put_test():
    return {"method": "put方法"}

@app.delete('/delete')
async def delete_test():
    return {"method": "delete方法"}


if __name__ == '__main__':
    uvicorn.run("04 路径操作装饰器方法:app", port=8080, reload=True)