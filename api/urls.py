from django.contrib import admin
from django.urls import path 
from .views import ACListAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('acs/', ACListAPIView.as_view()),


]
