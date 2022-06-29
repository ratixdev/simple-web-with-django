from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('profil/', include('profil.urls')),
	path('kontak/', include('kontak.urls')),
    path('home/', include('home.urls')),
    path('index/', include('index.urls')),
]
