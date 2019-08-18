from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="user1/base.html"), name='base'),
    path('register/', views.register, name='home'),
    path('login/', views.loginview, name='loginview'),
    path('home/', views.homeview),
    path('edit/', views.edit),
    path('logout/', views.logoutview, name='logoutview'),
]