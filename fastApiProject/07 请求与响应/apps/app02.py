from typing import Optional, Union

from fastapi import APIRouter

app02 = APIRouter()


@app02.get("/jobs")
async def get_jobs(kd: Optional[str], xl: Optional[str] = None, gj: Union[str, None] = None):  # 有默认参数,可以不填
    # 基于kd,xl,gj数据库查询岗位信息
    return {
        "kd": kd,
        "xl": xl,
        "gj": gj,
    }
