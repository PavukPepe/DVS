from django.contrib import admin
from django.urls import path
from . import views as v
from django.conf.urls.static import static as djstat
from django.urls import path

from engine_shop_prod import settings

urlpatterns = [
    path('', v.index, name='index'),
    path('/about', v.about, name='about'),
    path('/services', v.servises, name='servises'),
] + djstat(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

