from django.http import HttpResponse
from django.shortcuts import redirect

def restrict_customer(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.profile.user_role == 'Customer':
			return redirect('dashboard')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

