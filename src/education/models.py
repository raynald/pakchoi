from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Subject(models.Model):
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title', ]

class City(models.Model):
    name = models.CharField(max_length=50)

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
    school = models.CharField(max_length=50, null=True, blank=True)
    subjects = models.ManyToManyField(Subject)
    district = models.ForeignKey(District)
    picture = models.ImageField('Teacher picture',
                                upload_to='teacher_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    price = models.IntegerField(default=50)
    level = models.ForeignKey(Level, null=True, blank=True)
    achievement = models.TextField(max_length=1000, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    #rate = models.ForeignKey(Rating)

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
