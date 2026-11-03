from django.contrib import admin
from django.urls import path

admin.site.site_header = "Управление магазином"

admin.site.site_title = "Панель управления"

admin.site.index_title = "Панель управления"

urlpatterns = [
    path('admin/', admin.site.urls),
]

