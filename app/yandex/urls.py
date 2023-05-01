from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


schema_view = get_schema_view(
   openapi.Info(
      title="Yandex-Zen API",
      default_version='v-0.01',
      description="API для взаимодействия с Яндекс Дзен API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="myrza-96g@mail.ru"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('posts.urls')),
    path('', include('rest_framework.urls')),

    # documentation URL
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_doc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_doc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)