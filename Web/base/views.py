from django.shortcuts import redirect, render
from .models import Venta
from .forms import VentasForm

# Crud1.
def ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'app/Ventas/index.html', {'ventas': ventas })

def crear(request):
    formulario= VentasForm(request.POST or None)
    if(formulario.is_valid()):
        formulario.save()
        return redirect('ventas')
    return render(request, 'app/Ventas/crear.html', {'formulario': formulario})    

def eliminar(request, id):
    ventas = Venta.objects.get(nombre=id)
    ventas.delete()
    return redirect('ventas')

def editar(request, id):
    ventas = Venta.objects.get(nombre=id)
    formulario= VentasForm(request.POST or None, instance=ventas )
    if formulario.is_valid and request.POST:
        formulario.save()
        return redirect('ventas')
    return render(request, 'app/Ventas/editar.html', {'formulario':formulario})

# Crud2.


# vista.

def invitado(request):
    return render(request,'app/Invitado.html')

def usuario(request):
    return render(request,'app/Usuario.html')

def ingreso(request):
    return render(request,'app/Ing.html')

def nosotros(request):
    return render(request,'app/Inv/Nosotros.html')

def precio(request):
    return render(request,'app/Inv/Precio.html')

def contacto(request):
    return render(request,'app/Inv/Contacto.html')
