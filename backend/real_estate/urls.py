from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Real Estate Amdin'
admin.site.site_title = 'Real Estate Admin Panel'
admin.site.index_title = 'Welcome to the Real Estate administration'