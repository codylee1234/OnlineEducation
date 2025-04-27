from __future__ import unicode_literals

from datetime import datetime

from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"city name")
    desc = models.CharField(max_length=200, verbose_name=u"city desc")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        # verbose_name = u"城市"
        verbose_name = u"City"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    """
    课程机构
    """
    CATEGORY_CHOICE = (
        ('pxjg', "org"),
        ('xx', 'school'),
        ('gr', 'user'),
    )
    city = models.ForeignKey(City, verbose_name=u"city", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name=u"org name")
    desc = models.TextField(verbose_name=u"org desc")
    category = models.CharField(verbose_name="org type", max_length=30, choices=CATEGORY_CHOICE, default="xx")
    click_nums = models.IntegerField(default=0, verbose_name=u"clicks")
    fav_nums = models.IntegerField(default=0, verbose_name=u"collected")
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name=u"Logo")
    address = models.CharField(max_length=150, verbose_name=u"prg address")
    students = models.IntegerField(default=0, verbose_name=u"students number")
    course_nums = models.IntegerField(default=0, verbose_name=u"course number")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add time")

    class Meta:
        # verbose_name = u"课程机构"
        verbose_name = u"Course organization"
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        return self.teacher_set.all().count()

    def get_class_course(self):
        return self.course_set.order_by('-students')[:2]

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u"org", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name=u"teacher")
    work_years = models.IntegerField(default=0, verbose_name=u"working time", null=True, blank=True)
    work_company = models.CharField(max_length=50, verbose_name=u"work company", null=True, blank=True)
    # 如果模型字段设置blank=True，那么表单字段的required设置为False 。否则，required = True
    work_position = models.CharField(max_length=50, verbose_name=u"work position", null=True, blank=True)
    points = models.CharField(max_length=50, verbose_name=u"teach feature", null=True, blank=True)
    click_nums = models.IntegerField(default=0, verbose_name=u"clicks")
    fanv_nums = models.IntegerField(default=0, verbose_name=u"collected")
    image = models.ImageField(upload_to='teacher/%Y/%m', verbose_name=u"avatar", null=True, blank=True)
    age = models.IntegerField(verbose_name="age", default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"add time")

    class Meta:
        # verbose_name = u"教师"
        verbose_name = u"Teacher"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_course_num(self):
        return self.course_set.count()
