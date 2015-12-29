# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from authtools.models import User

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
    achievement = models.TextField(max_length=1000, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    create_by = models.ForeignKey(User)
    create_by.verbose_name = '创建者'

    def get_absolute_url(self):
        return "/teacher/%i/" % self.id

    def __unicode__(self):
        return self.full_name


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
    subjects = models.ManyToManyField(Subject)
    district = models.ForeignKey(District)
    picture = models.ImageField('Student picture',
                               upload_to='student_pics/%Y-%m-%d/',
                               null=True,
                               blank=True)
    requirement = models.TextField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return self.full_name

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

    def get_absolute_url(self):
        return "/problem/%i/" % self.id

    def __unicode__(self):
        return self.title


# class Event(models.Model):
#     teacher = models.ForeignKey(Teacher)
#     student = models.ForeignKey(Student)
