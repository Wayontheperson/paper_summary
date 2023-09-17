from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class SignForm(UserCreationForm):
    username = forms.CharField(max_length=10, help_text="아이디를 입력하세요")
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput,
        help_text='위의 비밀번호를 다시 입력하세요.',
    )

    class Meta:
        model = models.User
        fields = ("username","gender","password1", "password2")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return password1
