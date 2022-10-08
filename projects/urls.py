from django.contrib import admin
from django.urls import path
from databaseapp import views
from databaseapp.views import first_names

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_names/', views.first_names),
]
