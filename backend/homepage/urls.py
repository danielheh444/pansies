from rest_framework.routers import DefaultRouter
from homepage.views import PreviewViewApi


router = DefaultRouter()
router.register(r'preview', PreviewViewApi)


urlpatterns = []

urlpatterns.extend(router.urls)
