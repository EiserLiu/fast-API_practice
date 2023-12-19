import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apps.app01 import app01
from apps.app02 import app02
from apps.app03 import app03
from apps.app04 import app04
from apps.app05 import app05
from apps.app06 import app06
from apps.app07 import app07

app = FastAPI()

app.mount("/static", StaticFiles(directory="statics"))  # 静态文件的访问

app.include_router(app01, tags=["01 路径参数"])
app.include_router(app02, tags=["02 查询参数"])
app.include_router(app03, tags=["03 请求体数据"])
app.include_router(app04, tags=["04 form表单数据"])
app.include_router(app05, tags=["05 文件上传"])
app.include_router(app06, tags=["06 request对象"])
app.include_router(app07, tags=["07 相应参数"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)
