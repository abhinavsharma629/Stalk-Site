from django.urls import path
from . import views
urlpatterns = [
	# /common
    path('', views.index, name='index'),
]
