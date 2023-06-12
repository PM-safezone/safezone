from django.forms import ModelForm
from django import forms
from siteadmin_app.models import SiteAdmin


class SiteAdminCreationForm(ModelForm):
	name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'name-container',
				'type': 'text',
				'placeholder': 'name',
				'uname': 'uname',
				'required': True
			}
		)
	)
	image = forms.ImageField(
		required=True,
		widget=forms.ClearableFileInput(
			attrs={
				'class': 'image-container'
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
		model = SiteAdmin
		fields = ['name', 'image', 'management_locations', 'phone']




class SiteAdminDetailForm(SiteAdminCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].disabled = True

