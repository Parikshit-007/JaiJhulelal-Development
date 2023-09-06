
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from main.admin import upload_excel_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('main.urls')),
    path('admin/upload_excel/', upload_excel_view, name='upload_excel'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

