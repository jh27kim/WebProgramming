from pride import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pride/', include('pride.urls')),
    path('common/', include('common.urls')),
]
