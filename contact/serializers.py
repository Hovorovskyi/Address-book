from django.utils import timezone
from rest_framework import serializers
from contact.models import Contact, Event


class ContactShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'country', 'city', 'street', 'url', 'phone', 'image']


class EventSerializer(serializers.ModelSerializer):
    contacts = ContactShortSerializer(many=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date_time', 'location', 'contacts']


class EventCreateUpdateSerializer(serializers.ModelSerializer):
    contacts = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all())
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_time', 'location', 'contacts']

    def validate_date_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(f"The event can't be in the past.")
        return value
