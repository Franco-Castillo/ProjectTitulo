from django.urls import path
from . import views
from .views import invitado , usuario , ingreso, contacto, precio, nosotros, registro, ayuda

urlpatterns = [
    path('', invitado, name="Invitado"),
    path('Usuario/', usuario, name="Usuario"),
    path('Nosotros/', nosotros, name="Nosotros"),
    path('Precio/', precio, name="Precio"),
    path('Ingreso/', ingreso, name="Ingreso"),
    path('Contacto/', contacto, name="Contacto"),
    path('Ayuda/', ayuda, name="Ayuda"),
    #crud1
    path('Ventas/index', views.ventas, name="ventas"),
    path('Ventas/crear', views.crear, name="crear"),
    path('app/Ventas/editar/<str:id>', views.editar, name="editar"),
    path('app/Ventas/eliminar/<str:id>', views.eliminar, name="eliminar"),
    #crud2
    path('Gastos/index1', views.gastos, name="gastos"),
    path('Gastos/crear1', views.crear1, name="crear1"),
    path('app/Gastos/editar1/<str:id>', views.editar1, name="editar1"),
    path('app/Gastos/eliminar1/<str:id>', views.eliminar1, name="eliminar1"),
    #Usuario
    path('registro/', registro, name="registro"),
    
]
