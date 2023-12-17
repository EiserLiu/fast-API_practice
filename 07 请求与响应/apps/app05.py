from typing import List

from fastapi import APIRouter, File

app05 = APIRouter()


@app05.get("/file")
async def file(file: bytes = File()):
    # 适合小文件上传
    print(file, type(file))
    return {
        "file": len(file)
    }


@app05.get("/files")
async def files(files: List[bytes] = File()):
    # # 适合小文件上传
    # print(files, type(files))
    for file in files:
        print(len(file))
    return {
        "file": len(files)
    }
