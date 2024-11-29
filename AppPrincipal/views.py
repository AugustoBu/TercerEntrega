from django.shortcuts import render, redirect
from .forms import ProductoForm  
from .models import Producto

def inicio(request):
    return render(request, 'AppPrincipal/inicio.html')  

#Funcion Agregar Productos
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  
    else:
        form = ProductoForm()
    return render(request, 'AppPrincipal/agregar_producto.html', {'form': form})  

#Funcion Buscar Productos
def buscar_producto(request):
    query = request.GET.get('query')
    resultados = []
    if query:
        resultados = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'AppPrincipal/buscar_producto.html', {'resultados': resultados})