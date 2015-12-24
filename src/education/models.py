from __future__ import unicode_literals

from django.db import models


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
    achievement = models.TextField(max_length=1000, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return self.full_name


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
