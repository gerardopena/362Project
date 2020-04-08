from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('home/', views.IndexView.as_view(), name='homepage'),
    path('reserve/', views.WebsiteReserveView.as_view(), name='reservepage')

]