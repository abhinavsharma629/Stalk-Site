from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	# /student
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('success', views.success, name='success'),
    path('search', views.search, name='search'),
    path('number', views.number, name='number'),

] 
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
 #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)