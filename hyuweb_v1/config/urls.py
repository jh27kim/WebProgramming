from pride.views import base_views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pride/', include('pride.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'),
]
