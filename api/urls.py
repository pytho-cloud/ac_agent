from django.contrib import admin
from django.urls import path ,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'reviews', ReviewViewSet, basename='review')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('acs/', ACListAPIView.as_view()),
    path('', include(router.urls)),
    path('get-maintainence/', MaintenanceAPIView.as_view()),
    path('reviews/', ReviewsAPIView.as_view()),

]
