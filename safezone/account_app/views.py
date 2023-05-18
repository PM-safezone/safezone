from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy,  reverse

from account_app.forms import CreateAdminForm
from account_app.models import UserModel


# Create your views here.

class CreateAdminView(CreateView):
	model = UserModel
	form_class = CreateAdminForm
	success_url = reverse_lazy('login')
	template_name = 'account_app/create_admin.html'