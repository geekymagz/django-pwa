from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mywebsite import views as pwa_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mywebsite.urls', namespace='mywebsite')),

    # pwa route
    path('offline/', pwa_view.offline, name='offline'),
    path('sw.js', pwa_view.ServiceWorkerView.as_view(), name='sw.js',),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)