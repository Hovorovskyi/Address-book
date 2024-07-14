from contact.models import Contact, Event
from contact.serializers import ContactSerializer, EventSerializer, EventCreateUpdateSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'city']
    permission_classes = [permissions.AllowAny]


class EventViewSet(ModelViewSet):
    queryset = Event.objects.prefetch_related('contacts').all()
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['title', 'location', 'created_at', 'contacts']
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return EventCreateUpdateSerializer
        return EventSerializer
