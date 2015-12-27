from django import forms
from models import Teacher

class CreateTeacherForm(forms.ModelForm):

        class Meta:
            model = Teacher
            field = ['full_name', 'gender', 'school', 'department', 'picture']