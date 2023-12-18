import os
from typing import List

from fastapi import APIRouter, File, UploadFile

app05 = APIRouter()


@app05.post("/file")
async def get_file(file: bytes = File()):
    # 适合小文件上传
    print(file, type(file))
    return {
        "file": len(file)
    }


@app05.post("/files")
async def get_files(files: List[bytes] = File()):
    # # 适合小文件上传
    # print(files, type(files))
    for file in files:
        print(len(file))
    return {
        "file": len(files)
    }


@app05.post("/uploadFile")
async def get_uploadfile(file: UploadFile):
    # # 适合小文件上传
    print("file:", file)

    path = os.path.join("files", file.filename)
    # 文件保存
    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)
    return {
        "file": file.filename
    }


@app05.post("/uploadFiles")
async def get_uploadfiles(files: List[UploadFile]):
    # # 适合小文件上传
    print("file:", files)

    f = [file.filename for file in files]

    return {
        "names": f
    }
