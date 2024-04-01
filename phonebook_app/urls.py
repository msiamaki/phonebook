from django.urls import path, include
from rest_framework import routers
from .views import ContactViewSet

contact_router = routers.DefaultRouter()
contact_router.register('', ContactViewSet)


urlpatterns = [
    path('contacts/', include(contact_router.urls)),
]
