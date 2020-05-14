from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

import mainapp.views as mainapp

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mainapp.main, name="main"),
    path('products/', include('mainapp.urls', namespace='products')),
    path("products/all", mainapp.products, name="products_all"),
    path("products/home", mainapp.products, name="products_home"),
    path("products/office", mainapp.products, name="products_office"),
    path("products/modern", mainapp.products, name="products_modern"),
    path("products/classic", mainapp.products, name="products_classic"),
    path("contact/", mainapp.contact, name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
