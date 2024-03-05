from django.contrib import admin
# include necessary libraries
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("rest_app.urls"))
]