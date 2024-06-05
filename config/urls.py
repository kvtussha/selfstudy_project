from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('materials.urls', namespace='materials')),
   path('users/', include('users.urls', namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
