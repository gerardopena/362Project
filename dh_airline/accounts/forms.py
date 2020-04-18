# April 16, 2020
# Kyle Ear
# Gerardo Pena
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import Account

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")

	class Meta:
		model = Account
		fields = ("email","username","password1","password2")

class AccountUpdateForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ('email','username','first_name','last_name',)

	def clean_email(self):
		# check if email is available
		if self.is_valid():
			email = self.cleaned_data['email']
			# check if account exists
			try:
				account = Account.object.exclude(pk=self.instance.pk).get(email=email)
			except Account.DoesNotExist:
				return email
			raise forms.ValidationError('Email "%s" is already in use.' % account.email)

	def clean_username(self):
		# check if email is available
		if self.is_valid():
			username = self.cleaned_data['username']
			# check if account exists
			try:
				account = Account.object.exclude(pk=self.instance.pk).get(username=username)
			except Account.DoesNotExist:
				return username
			raise forms.ValidationError('Username "%s" is already in use.' % account.username)

	def clean_first_name(self):
		# check if email is available
		if self.is_valid():
			first_name = self.cleaned_data['first_name']
			# check if account exists
			try:
				account = Account.object.exclude(pk=self.instance.pk).get(first_name=first_name)
			except Account.DoesNotExist:
				return first_name

		def clean_last_name(self):
			# check if email is available
			if self.is_valid():
				last_name = self.cleaned_data['last_name']
				# check if account exists
				try:
					account = Account.object.exclude(pk=self.instance.pk).get(last_name=last_name)
				except Account.DoesNotExist:
					return last_name
