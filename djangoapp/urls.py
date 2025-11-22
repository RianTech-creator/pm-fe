from django.contrib import admin
from django.urls import path, include
from usuario.views import home_view  # importa a view da home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),  # raiz do site
    path('pedido/', include('pedido.urls')),
    path('produto/', include('produto.urls')),
    path('admin/', admin.site.urls),    
    path('usuario/', include('usuario.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)