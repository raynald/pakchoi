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

subject_full = Subject.objects.all()

SUBJECT_CHOICES = ()
for subject in subject_full:
    SUBJECT_CHOICES += (str(subject.id), subject.title),

class TeacherBookingForm(forms.Form):
    grade = forms.ChoiceField(choices = CHOICES, required=True, label='年级')
    subjects = forms.MultipleChoiceField(required=True,
                                               widget=forms.CheckboxSelectMultiple, choices=SUBJECT_CHOICES)
    # time =
    name = forms.CharField()
    mobile = forms.IntegerField()
    # TODO: payment