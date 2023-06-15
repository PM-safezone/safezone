from django.forms import ModelForm
from django import forms
from siteadmin_app.models import SiteAdmin


class SiteAdminCreationForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'name-container',
                'type': 'text',
                'placeholder': 'Name',
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
        model = SiteAdmin
        fields = ['name', 'image', 'management_locations', 'phone']


class SiteAdminUpdateForm(SiteAdminCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        MANAGEMENT_LOCATIONS_CHOICES = [
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
        self.fields['management_locations'].choices = MANAGEMENT_LOCATIONS_CHOICES

class SiteAdminDetailForm(SiteAdminCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True
