from typing import List

from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from models import *
from pydantic import BaseModel, validator

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
    # stus = await Student.all().values("name", "sno")
    # print(stus)

    # 一对多查询 多对多查询
    stu = await Student.get(name="刘泽普")

    print(stu.name)
    print(stu.sno)
    print(stu.clas_id)
    print(await stu.clas.values("name"))
    student = await Student.all().values("name", "clas__name")
    print(await stu.course.all().values("name", "teacher__name"))
    student = await Student.all().values("name", "clas__name", "course__name")

    return student


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


class StudentIn(BaseModel):
    name: str
    pwd: str
    sno: int
    clas_id: int
    courses: List[int] = []

    @validator("name")
    def name_mast_alpha(cls, value):
        assert value.isalpha(), "name must be alpha"
        return value

    @validator("sno")
    def sno_validate(cls, value):
        assert 0 < value < 100, "学号要在0到100之间"
        return value


@student_api.post("/")
async def addStudent(student_in: StudentIn):
    # 插入到数据库
    # 方式1
    # student = Student(name=student_in.name, pwd=student_in.pwd, sno=student_in.sno, _class_id=student_in.clas_id)
    # await student.save()  # 插入到数据库student表

    # 方式2
    student = await Student.create(name=student_in.name, pwd=student_in.pwd, sno=student_in.sno,
                                   clas_id=student_in.clas_id)

    # 多对多的关系绑定
    choose_courses = await Course.filter(id__in=student_in.courses)
    await student.course.add(*choose_courses)

    return student


@student_api.get("/{student_id}")
async def getStudent(student_id: int):
    student = await Student.get(id=student_id)
    return student


@student_api.put("/{student_id}")
async def upStudent(student_id: int, student_in: StudentIn):
    data = student_in.dict()
    courses = data.pop("courses")
    print(data)
    await Student.filter(id=student_id).update(**data)
    # 设置多对多的选修课
    edit_stu = await Student.get(id=student_id)
    choose_courses = await Course.filter(id__in=courses)
    await edit_stu.course.clear()
    await edit_stu.course.add(*choose_courses)

    return await Student.get(id=student_id)


@student_api.delete("/{student_id}")
async def upStudent(student_id: int):
    deleteCoune = await Student.filter(id=student_id).delete()
    if not deleteCoune:
        raise HTTPException(status_code=404, detail=f"主键为{student_id}的学生不存在")

    return {}
