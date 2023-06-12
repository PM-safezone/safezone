from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from account_app.models import UserModel


class CreateAdminForm(UserCreationForm):
	username = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'username-container',
				'type': 'text',
				'placeholder': 'id.',
				'uname': 'uname',
				'required': True
			}
		)
	)
	password1 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'class': 'password-container',
				'placeholder': 'password.',
				'uname': 'pwd',
				'required': True
			}
		)
	)
	password2 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'class': 'password2-container',
				'placeholder': 'password confirmation.',
				'uname': 'pwd2',
				'required': True
			}
		)
	)
	nickname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'nickname-container',
				'placeholder': 'name',
				'uname': 'name',
				'required': True
			}
		)
	)

	email = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'email-container',
				'placeholder': 'email.',
				'uname': 'email',
				'required': True
			}
		)
	)
	MANAGEMENT_LOCATIONS_CHOICES = [
		('placeholder', 'choice management location.'),  # placeholder
		('option1', '구역 1'),
		('option2', '구역 2'),
		('option3', '구역 3'),
	]
	management_locations = forms.ChoiceField(
		choices=MANAGEMENT_LOCATIONS_CHOICES,
		widget=forms.Select(
			attrs={
				'class': 'ml-container ml-select',
				'uname': 'ml',
				'required': True,
				'placeholder': 'choice management location.'
			}
		)
	)
	phone = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'phone-container',
				'placeholder': 'phone number',
				'uname': 'phone',
				'required': True
			}
		)
	)

	class Meta:
		model = UserModel
		fields = ('email', 'username', 'password1', 'password2', 'management_locations', 'phone')
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
		}


class AdminUpdateForm(CreateAdminForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].label = "ID"
		self.fields['nickname'].label = "Name"


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
				'placeholder': 'id',
				'required': True
			}
		)
	)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'class': 'password-container',
				'placeholder': 'password',
				'name': 'pwd',
				'required': True
			}
		)
	)
