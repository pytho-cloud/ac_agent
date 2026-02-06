from django.contrib import admin
from django.urls import path ,include
from .views import *
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
# router.register(r'reviews', ReviewViewSet, basename='review')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('acs/', ACListAPIView.as_view()),
    path('', include(router.urls)),
    path('get-maintainence/', MaintenanceAPIView.as_view()),
    path('reviews/', ReviewsAPIView.as_view()),
    path("contact/", ContactAPIView.as_view(), name="contact-api"),
    path('ac-filter-list/', ACView.as_view(), name='ac-list'),
    # path('post-enquiry/', BookServiceView.as_view()),
    path('products-acs/', ProductACAPIView.as_view()),
    path("product-sell-create/", ProductSellCreateAPIView.as_view()),
   path("post-enquiry/", EnquireAPIView.as_view(), name="post-enquirys"),


]
