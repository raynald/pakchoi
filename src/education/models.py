# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from authtools.models import User
import datetime
from haystack import indexes

GENDER_CHOICES = (
    ('M', '男'),
    ('F', '女'),
)

class Grade(models.Model):
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title', ]


class Subject(models.Model):
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title', ]

class City(models.Model):
    name = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    full_name.verbose_name = "姓名"
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    gender.verbose_name = "性别"
    school = models.CharField(max_length=50, null=True, blank=True)
    school.verbose_name = "学校"
    department = models.CharField(max_length=50, null=True, blank=True)
    department.verbose_name = "学院"
    subjects = models.ManyToManyField(Subject)
    grades = models.ManyToManyField(Grade)
    district = models.ForeignKey(District, null=True, blank=True)
    picture = models.ImageField('上传头像（请使用真实照片）',
                                upload_to='teacher_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    verify_picture = models.ImageField('学生证验证（学生证照片+手写边际教育）',
                                        upload_to='teacher_vers/%Y-%m-%d/',
                                       null=True,
                                       blank=True)
    available = models.CharField(max_length=200, null=True, blank=True)
    available.verbose_name = "可选时间"
    price = models.IntegerField(default=50)
    #TODO: price is related with level
    level = models.ForeignKey(Level, null=True, blank=True)
    mobile = models.IntegerField(default=1390000000)
    mobile.verbose_name = '手机号码'
    achievement = models.TextField(max_length=1000, null=True, blank=True)
    achievement.verbose_name = '战绩'
    description = models.TextField(max_length=1000, null=True, blank=True)
    description.verbose_name = '自我介绍'
    create_by = models.ForeignKey(User)
    create_by.verbose_name = '创建者'

    def get_absolute_url(self):
        return "/teacher/%i/" % self.id

    def __unicode__(self):
        return self.full_name


class TeacherIndex(indexes.SearchIndex, indexes.Indexable):
    name = indexes.CharField()
    school = indexes.CharField()
    subject = indexes.CharField(document=True, model_attr='Subject')
    grade = indexes.CharField(model_attr='Grade')
    district = indexes.CharField(model_attr='Distrct')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Teacher

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())


class Rating(models.Model):
    mobile = models.CharField(max_length=50)
    star = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField(max_length=200, null=True, blank=True)
    teacher = models.ForeignKey(Teacher)

    def __unicode__(self):
        return self.comment

    def get_hidden_mobile(self):
        return '%s****%s' % (self.mobile[:3], self.mobile[-4:])


class Student(models.Model):
    full_name = models.CharField(max_length=50)
    full_name.verbose_name = '学生姓名'
    subjects = models.ManyToManyField(Subject)
    subjects.verbose_name = '课程'
    grades = models.ManyToManyField(Grade)
    grades.verbose_name = '年级段'
    district = models.ForeignKey(District)
    district.verbose_name = '所在区域'
    picture = models.ImageField('Student picture',
                               upload_to='student_pics/%Y-%m-%d/',
                               null=True,
                               blank=True)
    picture.verbose_name = '学生照片'
    parent_mobile = models.IntegerField(default=1520000000)
    parent_mobile.verbose_name = '家长手机号'
    requirement = models.TextField(max_length=1000, null=True, blank=True)
    requirement.verbose_name = '学生要求'
    create_by = models.ForeignKey(User)
    create_by.verbose_name = '创建者'

    def __unicode__(self):
        return self.full_name

    def get_absolute_url(self):
        return "/student/%i/" % self.id


class Problem(models.Model):
    title = models.CharField(max_length=50)
    title.verbose_name = '难题类别'
    picture = models.ImageField('上传问题相关图片',
                                 upload_to='problem_pics/%Y-%m-%d/',
                                 null=True,
                                 blank=True)
    picture.verbose_name = '问题配图'
    description = models.TextField(max_length=1000, null=True, blank=True)
    description.verbose_name = '问题描述'
    author = models.ForeignKey(User)
    author.verbose_name = '上传者'
    created_at = models.DateTimeField(auto_now_add=True)
    created_at.verbose_name = '创建时间'
    updated_at = models.DateTimeField(auto_now=True)
    updated_at.verboes_name = '上次修改时间'
    solved = models.BooleanField(default=False)

    def get_absolute_url(self):
        return "/problem/%i/" % self.id

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    picture = models.ImageField('答案相关图片',
                                upload_to='answer_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    picture.verbose_name = '答案配图'
    description = models.TextField(max_length=1000, null=True, blank=True)
    description.verbose_name = '答案描述'
    problem = models.ForeignKey(Problem)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at.verbose_name = '创建时间'
    updated_at = models.DateTimeField(auto_now=True)
    updated_at.verboes_name = '上次修改时间'


INIT = 0
# STUDENT_PAID = 1
TEACHER_CONFIRMED = 1
STUDENT_RATED = 2
# FINISH = 4

STATUS_CHOICES = (
    (INIT, "订单生成"),
    # 学生付款后才能生成订单 (STUDENT_PAID, '学生已付款'),
    (TEACHER_CONFIRMED, '老师已确认'),
    (STUDENT_RATED, '学生已评价'),
    # (FINISH, '已完成'),
)

TIME_CHOICES = (
    (1, '上午'),
    (2, '下午'),
    (3, '晚上'),
)

class Order(models.Model):
    user_teacher = models.ForeignKey(User, related_name="user_teacher")
    user_student = models.ForeignKey(User, related_name="user_student")
    subjects = models.ManyToManyField(Subject)
    subjects.verbose_name = '学科'
    date = models.DateField(default=datetime.date.today)
    date.verbose_name = '日期'
    state =  models.IntegerField(choices=STATUS_CHOICES, default=INIT)
    time = models.IntegerField(choices=TIME_CHOICES, default=3)
    time.verbose_name = '期望时间段'
    teacher_name = models.CharField(max_length=20, default="Jason Marz")
    teacher_name.verbose_name = '老师姓名'
    student_name = models.CharField(max_length=20, default="John Doe")
    student_name.verbose_name = '学生姓名'
    teacher_mobile = models.IntegerField(default=1390000000)
    teacher_mobile.verbose_name = '老师手机号'
    parent_mobile = models.IntegerField(default=1520000000)
    parent_mobile.verbose_name = '家长手机号'

    def __unicode__(self):
        return self.teacher_name + self.student_name


