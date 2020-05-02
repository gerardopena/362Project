# April 18, 2020
# Kyle Ear
# Gerardo Pena
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save

from flights.models import Flight

#User = get_user_model()

class MyAccountManager(BaseUserManager):
	
	def create_user(self,email,username,password=None):
		if not email:
			raise ValueError("Users must have an email address")
		if not username:
			raise ValueError("Users must have a username")

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,username,password):
		user = self.create_user(
			email = self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

<<<<<<< HEAD

class Account(AbstractBaseUser):
	email = models.EmailField(verbose_name="email",max_length=60,unique=True)
=======
	def id(email):
		return email.id

class Account(AbstractBaseUser, models.Model):
	email = models.EmailField(verbose_name="email",max_length=60,unique=True, primary_key=True)
>>>>>>> 313d1725625d1766b703f1af6171077c4f9b3327
	username = models.CharField(max_length=30,unique=True)
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last_login',auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	# Above are required
	# Can add further fields like first name, last name, address, cc#
	first_name = models.CharField(max_length=30,default='')
	last_name  = models.CharField(max_length=30,default='')
	street_address = models.CharField(max_length=30,default='')
	city_address = models.CharField(max_length=30,default='')
	state_address = models.CharField(max_length=2,default='')
	zip_address = models.IntegerField(default=0)
	
	flights = models.ManyToManyField(Flight, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	object = MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self,perm,obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	flights = models.ManyToManyField(Flight, blank=True)

	def __str__(self):
		return self.user.username


def post_save_profile_create(sender, instance, created, *args, **kwargs):
	if created:
		Account.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
