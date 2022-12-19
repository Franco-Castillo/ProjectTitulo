from django.urls import path
from . import views
from .views import invitado , usuario , ingreso, contacto, precio, nosotros, registro

urlpatterns = [
    path('', invitado, name="Invitado"),
    path('Usuario/', usuario, name="Usuario"),
    path('Nosotros/', nosotros, name="Nosotros"),
    path('Precio/', precio, name="Precio"),
    path('Ingreso/', ingreso, name="Ingreso"),
    path('Contacto/', contacto, name="Contacto"),
    path('Ventas/index', views.ventas, name="ventas"),
    path('Ventas/crear', views.crear, name="crear"),
    path('app/Ventas/editar/<str:id>', views.editar, name="editar"),
    path('app/Ventas/eliminar/<str:id>', views.eliminar, name="eliminar"),
    path('registro/', registro, name="registro"),
    
]
