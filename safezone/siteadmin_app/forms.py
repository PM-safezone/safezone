from django.forms import ModelForm
from siteadmin_app.models import SiteAdmin


class SiteAdminCreationForm(ModelForm):
	class Meta:
		model = SiteAdmin
		fields = ['name', 'image', 'management_locations', 'phone']
