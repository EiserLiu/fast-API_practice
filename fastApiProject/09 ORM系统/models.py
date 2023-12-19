from tortoise.models import Model
from tortoise import fields


# 选课系统

class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="姓名")
    pwd = fields.CharField(max_length=32, description="密码")
    sno = fields.IntField(description="学号")

    # 一对多
    _class = fields.ForeignKeyField("models._Class", related_name="Students")

    # 多对多
    course = fields.ManyToManyField("models.Course", related_name="Students", description="学生选课表")


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="课程名称")
    teacher = fields.ForeignKeyField("models.Teacher")
    addr = fields.CharField(max_length=32, description="教室", default="")


class _Class(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="班级名称")


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="教师名称")
    pwd = fields.CharField(max_length=32, description="密码")
