from django.urls import path,re_path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
	# /teacher
    path('', views.regisearch, name='regisearch'),
    path('login', LoginView.as_view(template_name='teacher/logyouin.html'), name="login"),
    path('logout', LogoutView.as_view(template_name='teacher/logyouout.html'), name="logout"),
    path('register', views.register, name='register'),
    path('detail', views.detail, name='detail'),
    path('profile', views.profile, name='profile'),
    path('profile/search', views.search, name='search'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/info', views.info, name='info'),
    path('profile/all_info', views.all_info, name='all_info'),
]
