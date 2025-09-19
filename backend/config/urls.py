from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # Frontend landing page
    path('', home_view, name='home'),
]

# Serve media files (user uploads)
# In small deployments (e.g., Railway), it's acceptable to let Django serve media.
# For larger scale, move media to an external storage (S3) or a CDN.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
