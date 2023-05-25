from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin

from siteadmin_app.forms import SiteAdminCreationForm
from siteadmin_app.models import SiteAdmin


# Create your views here.


class SiteAdminCreateView(CreateView):
	model = SiteAdmin
	form_class = SiteAdminCreationForm
	template_name = 'siteadmin_app/create.html'

	def get_success_url(self):
		return reverse_lazy('siteadmin_app:list')


class SiteAdminListView(ListView):
	model = SiteAdmin
	context_objecct_name = 'siteadmin_list'
	template_name = 'siteadmin_app/list.html'
	paginate_by = 20


class SiteAdminDetailView(DetailView, FormMixin):
	model = SiteAdmin
	context_object_name = 'target_siteadmin'
	template_name = 'siteadmin_app/detail.html'
