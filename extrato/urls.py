from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('novo_valor/', views.novo_valor, name='novo_valor'),
    path('view_extrato/', views.view_extrato, name='view_extrato'),
    path('exportar_pdf/', views.exportar_pdf, name='exportar_pdf')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
