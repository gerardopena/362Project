# April 16, 2020 
# Kyle Ear
# Gerardo Pena
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.forms import RegistrationForm, AccountUpdateForm
# Create your views here.

def signup_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('homepage')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'accounts/signup.html', context)


def account_view(request):

	if not request.user.is_authenticated:
		return redirect("login")
	
	context = {}

	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
	else:
		form = AccountUpdateForm(
			initial= {
				'email': request.user.email,
				'username': request.user.username
			}
		)

	context['account_form'] = form

	return render(request, 'accounts/account.html', context)