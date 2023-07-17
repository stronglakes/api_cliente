from rest_framework.routers import DefaultRouter
from api.views import ClienteViewSet

router = DefaultRouter()

router.register('api/cliente', ClienteViewSet)
#Otras rutas

urlpatterns = []

urlpatterns += router.urls
