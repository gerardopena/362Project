# April 18, 2020
# Kyle Ear
# Gerardo Pena
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.forms import RegistrationForm, AccountUpdateForm
#from cart.models import Order
#from . import Account
# Create your views here.
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView
from . import views

def signup_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)  # request.FILES is show the selected image or file

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
			return redirect('homepage')
	else:
		form = AccountUpdateForm(
			initial= {
				'username': request.user.username,
				'first_name': request.user.first_name,
				'last_name': request.user.last_name,
				'email': request.user.email,
				'street_address': request.user.street_address,
				'city_address': request.user.city_address,
				'state_address': request.user.state_address,
				'zip_address': request.user.zip_address,

			}
		)
	context['account_form'] = form

	return render(request, 'accounts/account.html', context)
<<<<<<< HEAD
=======

""" def cart_profile(request):
	my_user_profile = Account.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	context = {
		'my_orders': my_orders
	}

	return render(request, "cartpage.html", context) """
>>>>>>> 313d1725625d1766b703f1af6171077c4f9b3327
