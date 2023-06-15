from django import forms
from django.contrib.auth import authenticate

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from account_app.models import UserModel


class CreateAdminForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'username-container',
                'type': 'text',
                'placeholder': 'ID',
                'uname': 'uname',
                'required': True
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'password-container',
                'placeholder': 'Password',
                'uname': 'pwd',
                'required': True
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'password2-container',
                'placeholder': 'Password Confirmation',
                'uname': 'pwd2',
                'required': True
            }
        )
    )
    nickname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'nickname-container',
                'placeholder': 'Name',
                'uname': 'name',
                'required': True
            }
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'email-container',
                'placeholder': 'Email',
                'uname': 'email',
                'required': True
            }
        )
    )
    MANAGEMENT_LOCATIONS_CHOICES = [
        ('placeholder', 'Choose Your Location'),  # placeholder
        ('option1', '구역 1'),
        ('option2', '구역 2'),
        ('option3', '구역 3'),
        ('option4', '구역 4'),
        ('option5', '구역 5'),
        ('option6', '구역 6'),
        ('option7', '구역 7'),
        ('option8', '구역 8'),
        ('option9', '구역 9'),
    ]
    management_locations = forms.ChoiceField(
        choices=MANAGEMENT_LOCATIONS_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'ml-container ml-select',
                'uname': 'ml',
                'required': True,
                'placeholder': 'Choose Your Location'
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'phone-container',
                'placeholder': 'Phone Number',
                'uname': 'phone',
                'required': True
            }
        )
    )

    class Meta:
        model = UserModel
        fields = ('email', 'username', 'password1', 'password2', 'management_locations', 'phone', 'nickname')
        labels = {
            'username': '아이디',
            'password1': '비밀번호',
            'password2': '비밀번호 확인',
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
            'email': None,
            'nickname': None,
        }


class AdminUpdateForm(CreateAdminForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "ID"
        self.fields['nickname'].label = "Admin Name"


class AdminDetailForm(AdminUpdateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password1']
        del self.fields['password2']

        for field in self.fields:
            self.fields[field].disabled = True


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'username-container',
                'type': 'text',
                'name': 'uname',
                'placeholder': 'ID',
                'required': True
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'password-container',
                'placeholder': 'Password',
                'name': 'pwd',
                'required': True
            }
        )
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "아이디나 비밀번호가 틀렸습니다.",
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data