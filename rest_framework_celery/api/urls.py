from rest_framework.routers import DefaultRouter
from api.views import URLViewSet

router = DefaultRouter(trailing_slash=False)
router.register('request', URLViewSet, base_name='url_view')

urlpatterns = router.urls
