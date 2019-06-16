from datetime import datetime

from django.db import models

from users.models import User
from courses.models import Course


# Create your models here.
class UserAsk(models.Model):
    """
    用户咨询
    """
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    course_name = models.CharField(max_length=50, verbose_name="课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


class CourseComment(models.Model):
    """
    课程评论
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, verbose_name="评论", on_delete=models.DO_NOTHING)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, verbose_name="评论", on_delete=models.DO_NOTHING)
    fav_id = models.IntegerField(default=0, verbose_name="数据ID")
    fav_type = models.CharField(choices=((1, "课程"), (2, "课程机构"), (3, "讲师")), max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    """
    用户消息
    """
    user = models.IntegerField(default=0, verbose_name="接受用户")  # 所有用户为0， 否则具体用户为用户ID
    message = models.CharField(max_length=500, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="消息时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(User, verbose_name="用户", on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.DO_NOTHING)
    add_tiem = models.DateTimeField(default=datetime.now, verbose_name="开始学习时间")

    class Meta:
        verbose_name = "学习课程"
        verbose_name_plural = verbose_name
