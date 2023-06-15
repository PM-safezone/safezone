from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView

from siteadmin_app.forms import SiteAdminCreationForm, SiteAdminDetailForm
from siteadmin_app.models import SiteAdmin


# Create your views here.

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class SiteAdminCreateView(CreateView):
	model = SiteAdmin
	form_class = SiteAdminCreationForm
	template_name = 'siteadmin_app/create.html'

	def get_success_url(self):
		return reverse_lazy('siteadmin_app:list')


@method_decorator(login_required, 'get')
class SiteAdminListView(ListView):
	model = SiteAdmin
	context_objecct_name = 'siteadmin_list'
	template_name = 'siteadmin_app/list.html'
	paginate_by = 12

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		page_range = range(1, context['page_obj'].paginator.num_pages + 1)
		context['page_range'] = page_range
		return context
	# 페이지를 모두 표시하기 위해 넣음

# class SiteAdminDetailView(DetailView):
# 	model = SiteAdmin
# 	context_object_name = 'target_siteadmin'
# 	template_name = 'siteadmin_app/detail.html'


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class SiteAdminUpdateView(UpdateView):
	model = SiteAdmin
	form_class = SiteAdminCreationForm
	template_name = 'siteadmin_app/update.html'
	context_object_name = 'target_siteadmin'

	def get_success_url(self):
		return reverse_lazy('siteadmin_app:detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class SiteAdminDeleteView(DeleteView):
	model = SiteAdmin
	context_object_name = 'target_siteadmin'
	template_name = 'siteadmin_app/delete.html'
	success_url = reverse_lazy('siteadmin_app:list')


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class SiteAdminDetailView(UpdateView):
	model = SiteAdmin
	form_class = SiteAdminDetailForm
	context_object_name = 'target_siteadmin'
	template_name = 'siteadmin_app/detail.html'
