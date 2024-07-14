from contact.views import ContactViewSet, EventViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('contact', ContactViewSet, basename='contact')
router.register('event', EventViewSet, basename='event')

urlpatterns = router.urls
