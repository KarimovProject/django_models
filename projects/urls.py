from django.contrib import admin
from django.urls import path
from databaseapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_names/', views.first_name),
]
