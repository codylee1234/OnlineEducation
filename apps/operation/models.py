from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
from course.models import Course

# Create your models here.


class UserAsk(models.Model):
    """用户想要学习表单"""

    name = models.CharField(max_length=20, verbose_name=u"name", help_text='can not be blank', error_messages={'blank': 'can not be blank'})
    mobile = models.CharField(max_length=11, verbose_name=u"phone")
    # 当字段过小的时候  不会显示搜索框
    course_name = models.CharField(max_length=50, verbose_name=u"course name")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add time")

    class Meta:
        # verbose_name = u"用户咨询"
        verbose_name = u"User Consultation"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}add success".format(self.name)


class CourseComment(models.Model):
    """课程评论"""

    user = models.ForeignKey(UserProfile, verbose_name=u'user', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=u'course', on_delete=models.CASCADE)
    comments = models.CharField(verbose_name=u'comment', max_length=200)
    add_time = models.DateTimeField(verbose_name=u'add time', default=datetime.now)

    class Meta:
        # verbose_name = '课程评论'
        verbose_name = 'Course Review'
        verbose_name_plural = verbose_name

    def __str__(self):
       return "{0}add《{1}》comment".format(self.user, self.course)


class UserFavorite(models.Model):
    """用户收藏"""

    FAV_TYPE = (
        (1, 'course'),
        (2, 'course org'),
        (3, 'teacher'),
    )

    user = models.ForeignKey(UserProfile, verbose_name=u'user', on_delete=models.CASCADE)
    fav_id = models.IntegerField(verbose_name=u'data id', default=0)
    fav_type = models.IntegerField(verbose_name=u'collect type', choices=FAV_TYPE, default=1)
    add_time = models.DateTimeField(verbose_name=u'add time', default=datetime.now)

    class Meta:
        # verbose_name = u'用户收藏'
        verbose_name = u'User Collection'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(verbose_name=u'user', default=0)
    message = models.CharField(verbose_name=u'message', max_length=500)
    has_read = models.BooleanField(verbose_name=u'readed', default=False)
    add_time = models.DateTimeField(verbose_name=u'add time', default=datetime.now)

    class Meta:
        # verbose_name = '用户消息'
        verbose_name = 'User Messange'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    """用户课程"""
    user = models.ForeignKey(UserProfile, verbose_name=u'user', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=u'course', on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name=u'add time', default=datetime.now)

    class Meta:
        # verbose_name = '用户课程'
        verbose_name = 'User Course'
        verbose_name_plural = verbose_name




