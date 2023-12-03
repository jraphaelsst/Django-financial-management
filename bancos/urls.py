from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('gerenciar_bancos/', views.gerenciar_bancos, name='gerenciar_bancos'),
    path('cadastrar_banco/', views.cadastrar_banco, name='cadastrar_banco'),
    path('deletar_banco/<int:id>', views.deletar_banco, name='deletar_banco'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)