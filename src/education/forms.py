# -*- coding: utf-8 -*-

from django import forms
from models import Teacher, Subject

CHOICES = (
    ('1', '小学一年级'),
    ('2', '小学二年级'),
    ('3', '小学三年级'),
    ('4', '小学四年级'),
    ('5', '小学五年级'),
    ('6', '小学六年级'),
    ('7', '初中一年级'),
)

TIME_CHOICES = (
    ('1', '上午'),
    ('2', '下午'),
    ('3', '晚上'),
)

subject_full = Subject.objects.all()

SUBJECT_CHOICES = ()
for subject in subject_full:
    SUBJECT_CHOICES += (str(subject.id), subject.title),

class TeacherBookingForm(forms.Form):
    grade = forms.ChoiceField(choices = CHOICES, required=True, label='年级')
    subjects = forms.MultipleChoiceField(required=True,
                                               widget=forms.CheckboxSelectMultiple, choices=SUBJECT_CHOICES)
    prefered_date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}), label='日期')
    prefered_time = forms.ChoiceField(choices = TIME_CHOICES, required=True, label='时间')
    name = forms.CharField(label='学生姓名')
    mobile = forms.IntegerField(label='家长联系电话')
    # TODO: problem =
    # TODO: payment =


class StudentBookingForm(forms.Form):
    grade = forms.ChoiceField(choices = CHOICES, required=True, label='年级')
    subjects = forms.MultipleChoiceField(required=True,
                                         widget=forms.CheckboxSelectMultiple, choices=SUBJECT_CHOICES)
    prefered_date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}), label='日期')
    prefered_time = forms.ChoiceField(choices = TIME_CHOICES, required=True, label='时间')
    name = forms.CharField(label='学生姓名')
    mobile = forms.IntegerField(label='家长联系电话')
    # TODO: problem =
    # TODO: payment =