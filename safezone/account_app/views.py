from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from account_app.forms import CreateAdminForm, AdminUpdateForm, AdminProfileForm
from account_app.models import UserModel
from account_app.decorators import admin_ownership_required


# Create your views here.
has_ownership = [admin_ownership_required, login_required]


class CreateAdminView(CreateView):
	model = UserModel
	form_class = CreateAdminForm
	success_url = reverse_lazy('account_app:login')
	template_name = 'account_app/create_admin.html'


# class AdminProfileView(DetailView):
# 	model = UserModel
# 	form_class = AdminUpdateForm
# 	context_object_name = 'target_user'
# 	template_name = 'account_app/profile.html'
class AdminProfileView(UpdateView):
	model = UserModel
	form_class = AdminProfileForm
	context_object_name = 'target_user'
	template_name = 'account_app/profile.html'


	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		# Disable or set fields as read-only
		form.fields['username'].disabled = True
		form.fields['email'].disabled = True
		form.fields['management_locations'].disabled = True
		form.fields['phone'].disabled = True
		# Add more fields to disable or set as read-only as needed
		return form



@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminProfileUpdateView(UpdateView):
	model = UserModel
	form_class = AdminUpdateForm
	context_object_name = 'target_user'
	success_url = reverse_lazy('account_app:login')
	template_name = 'account_app/update_admin.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminDeleteView(DeleteView):
	model = UserModel
	context_object_name = 'target_user'
	success_url = reverse_lazy('account_app:login')
	template_name = 'account_app/delete_admin.html'

# def get_success_url(self):
# 	return reverse('account_app:login')
