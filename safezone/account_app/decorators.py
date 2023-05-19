from django.http import HttpResponseForbidden

from safezone.account_app.models import UserModel

def admin_ownership_required(func):
	def decorated(request, *args, **kwargs):
		user = UserModel.objects.get(pk=kwargs['pk'])
		if user != request.user:
			return HttpResponseForbidden()
		return func(request, *args, **kwargs)
	return decorated