from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy,  reverse

from account_app.forms import CreateAdminForm, AdminUpdateForm
from account_app.models import UserModel



# Create your views here.

class CreateAdminView(CreateView):
	model = UserModel
	form_class = CreateAdminForm
	success_url = reverse_lazy('account_app:login')
	template_name = 'account_app/create_admin.html'


class AdminProfileView(DetailView):
	model = User
	context_object_name = 'target_user'
	template_name = 'account_app/profile.html'


class AdminProfileUpdateView(UpdateView):
	model = UserModel
	form_class = AdminUpdateForm
	success_url = reverse_lazy('account_app:login')
	template_name = 'account_app/update_admin.html'