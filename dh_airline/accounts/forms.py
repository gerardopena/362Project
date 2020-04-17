# April 16, 2020
# Kyle Ear
# Gerardo Pena
from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Account

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")
	
	class Meta:
		model = Account
		fields = ("email","username","password1","password2")

class AccountUpdateForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ('email','username')

	def clean_email(self):
		# check if email is available
		if self.is_valid():
			email = self.cleaned_data['email']
			# check if account exists
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
			except Account.DoesNotExist:
				return email
			raise forms.ValidationError('Email "%s" is already in use.' % account.email)

	def clean_username(self):
		# check if email is available
		if self.is_valid():
			username = self.cleaned_data['username']
			# check if account exists
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
			except Account.DoesNotExist:
				return username
			raise forms.ValidationError('Username "%s" is already in use.' % account.username)

	