from django.contrib import admin
from django.urls import path, re_path, include 
from django.conf.urls.static import static
from django.conf import settings 
from django.views.generic import TemplateView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('src_api.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name = 'frontend/index.html'))]