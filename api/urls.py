from rest_framework.routers import DefaultRouter
from api.views import RouteViewSet, LocationViewSet

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'route', RouteViewSet)
router.register(r'location', LocationViewSet)

urlpatterns = router.urls