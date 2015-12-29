# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.core.urlresolvers import reverse


my_default_errors = {
    'required': '这个是必填项目!',
}

class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False, label="记住我")

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["username"].widget.input_type = "email"  # ugly hack
        self.fields["username"].label = "邮箱地址"
        self.fields["username"].error_messages = my_default_errors
        self.fields["password"].label = "密码"
        self.fields["password"].error_messages = my_default_errors

        self.helper.layout = Layout(
            Field('username', placeholder="请输入邮箱地址", autofocus=""),
            Field('password', placeholder="请输入密码"),
            HTML('<a href="{}">忘记密码?</a>'.format(
                reverse("accounts:password-reset"))),
            Field('remember_me'),
            Submit('sign_in', '登录',
                   css_class="btn btn-lg btn-primary btn-block"),
            )


class SignupForm(authtoolsforms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].widget.input_type = "email"  # ugly hack
        self.fields["email"].label = "电子邮箱"
        self.fields["email"].error_messages = my_default_errors
        self.fields["name"].label = "用户名"
        self.fields["name"].error_messages = my_default_errors
        self.fields["password1"].label = "密码"
        self.fields["password1"].error_messages = my_default_errors
        self.fields["password2"].label = "确认密码"
        self.fields["password2"].error_messages = my_default_errors
        self.fields["password2"].help_text = "为确认密码,请输入相同的密码"

        self.helper.layout = Layout(
            Field('email', placeholder="输入电子邮箱地址", autofocus=""),
            Field('name', placeholder="输入用户名"),
            Field('password1', placeholder="输入密码"),
            Field('password2', placeholder="重新输入密码"),
            Submit('sign_up', '注册', css_class="btn-warning"),
            )


class PasswordChangeForm(authforms.PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('old_password', placeholder="Enter old password",
                  autofocus=""),
            Field('new_password1', placeholder="Enter new password"),
            Field('new_password2', placeholder="Enter new password (again)"),
            Submit('pass_change', 'Change Password', css_class="btn-warning"),
            )


class PasswordResetForm(authtoolsforms.FriendlyPasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('email', placeholder="Enter email",
                  autofocus=""),
            Submit('pass_reset', 'Reset Password', css_class="btn-warning"),
            )


class SetPasswordForm(authforms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('new_password1', placeholder="Enter new password",
                  autofocus=""),
            Field('new_password2', placeholder="Enter new password (again)"),
            Submit('pass_change', 'Change Password', css_class="btn-warning"),
            )
