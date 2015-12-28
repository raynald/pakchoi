# -*- coding: utf-8 -*-

from django import forms
from models import Teacher

CHOICES = (
    ('1', '小学一年级'),
    ('2', '小学二年级'),
    ('3', '小学三年级'),
    ('4', '小学四年级'),
    ('5', '小学五年级'),
    ('6', '小学六年级'),
    ('7', '初中一年级'),
)

class TeacherBookingForm(forms.Form):
    grade = forms.ChoiceField(choices = CHOICES, required=True, label='年级')
    # TODO: subjects = forms.
    # TODO: time =
    name = forms.CharField()
    mobile = forms.IntegerField()
