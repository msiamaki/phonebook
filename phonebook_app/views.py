from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Contact
from .serializers import ContactSerializer

# Create your views here.


class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all().order_by("first_name")

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
