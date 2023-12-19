from fastapi import APIRouter, Request
from models import *
from pydantic import BaseModel
from typing import List, Union
from fastapi.templating import Jinja2Templates

student_api = APIRouter()


@student_api.get("/")
async def getAllStudent():
    # students = await Student.all()  # Queryset: [Student(),Student(),Student()]
    # print("students", students)
    #
    # for stu in students:
    #     print(stu.name, stu.sno)

    # 过滤查询 filter   返回模型对象列表
    # students = await Student.filter(_class_id=5)
    # print("student", students)
    # for stu in students:
    # print(stu.name, stu.sno)
    # 过滤查询 get  返回模型类型对象
    # stu = await Student.get(id=2)
    # print(stu.name)

    # 模糊查询

    # stus = await Student.filter(sno__gt=20)
    # stus = await Student.filter(sno__in=[1, 24])
    # stus = await Student.filter(sno__range=[1, 24])
    # for stu in stus:
    #     print(stu.name)

    # values 查询
    # stus = await Student.filter(sno__range=[1,30])
    # stus = await Student.all().values("name")
    stus = await Student.all().values("name", "sno")
    # print(stus)

    return {

        "操作": stus
    }


@student_api.get("/index.html")
async def getAllStudent(request: Request):
    templates = Jinja2Templates(directory="templates")
    students = await Student.all()

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "students": students
        }
    )


@student_api.post("/")
def addStudent():
    return {
        "操作": "添加学生"
    }


@student_api.get("/{student_id}")
def getStudent(student_id: int):
    return {
        "操作": f"查看id={student_id}的学生"
    }


@student_api.put("/{student_id}")
def upStudent(student_id: int):
    return {
        "操作": f"更新id={student_id}的学生"
    }


@student_api.delete("/{student_id}")
def upStudent(student_id: int):
    return {
        "操作": f"删除id={student_id}的学生"
    }
