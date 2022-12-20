from django.shortcuts import redirect, render
from .models import Venta, Gasto
from .forms import VentasForm, RegistroUsuario , GastosForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Crud1.
def ventas(request):
    ventas = Venta.objects.all()
    suma = 0
    for venta in ventas: 
        suma += venta.precio

    return render(request, 'app/Ventas/index.html', {'ventas': ventas , 'total': suma})

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

#---------------------------------------------------------------------------------
# Crud2.

def gastos(request):
    gastos = Gasto.objects.all()
    suma1 = 0
    for gasto in gastos: 
        suma1 += gasto.precio
    return render(request, 'app/Gastos/index1.html', {'gastos': gastos , 'total1': suma1})

def crear1(request):
    formulario= GastosForm(request.POST or None)
    if(formulario.is_valid()):
        formulario.save()
        return redirect('gastos')
    return render(request, 'app/Gastos/crear1.html', {'formulario': formulario})    

def eliminar1(request, id):
    gastos = Gasto.objects.get(fecha=id)
    gastos.delete()
    return redirect('gastos')

def editar1(request, id):
    gastos = Gasto.objects.get(fecha=id)
    formulario= GastosForm(request.POST or None, instance=gastos )
    if formulario.is_valid and request.POST:
        formulario.save()
        return redirect('gastos')
    return render(request, 'app/Gastos/editar1.html', {'formulario':formulario})

#---------------------------------------------------------------------------------
# Crud3.



# registro de Usuarios
def registro(request):
    data = {
        'form':RegistroUsuario()
    }

    if request.method == 'POST':
        formulario = RegistroUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado")
            return redirect(to="Usuario")
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)

# vista.

def invitado(request):
    return render(request,'app/Invitado.html')

#------------------------------------------------------
def usuario(request):
    ventas = Venta.objects.all()
    suma = 0
    for venta in ventas: 
        suma += venta.precio
        pass
    gastos = Gasto.objects.all()
    suma1 = 0
    for gasto in gastos: 
        suma1 += gasto.precio
        pass
    return render(request,'app/Usuario.html',{'ventas': ventas , 'total': suma ,'gastos': gastos , 'total1': suma1})
    
#-------------------------------------------------------
def ingreso(request):
    return render(request,'app/Ing.html')

def nosotros(request):
    return render(request,'app/Inv/Nosotros.html')

def precio(request):
    return render(request,'app/Inv/Precio.html')

def contacto(request):
    return render(request,'app/Inv/Contacto.html')

def ayuda(request):
    return render(request,'app/Usu/Ayuda.html')