from rest_framework import routers
from .api import DogViewSet, CatViewSet
from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="PetDex API",
        default_version='v1',
        description="API documentation for PetDex",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@petdex.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('api/dogs', DogViewSet, 'dogs')
router.register('api/cats', CatViewSet, 'cats')

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)

urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)