from django.shortcuts import redirect , render

def login_redirect(request):
	return render(request,'accounts/login.html')
