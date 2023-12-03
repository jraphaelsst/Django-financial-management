from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('definir_despesas/', views.definir_despesas, name='definir_despesas'),
    path('ver_despesas/', views.ver_despesas, name='ver_despesas'),
    path('apagar_despesa/<int:id>', views.apagar_despesa, name='apagar_despesa'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)