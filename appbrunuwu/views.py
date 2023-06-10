from django.shortcuts import render, redirect
from .forms import Clase1Form, Clase2Form, Clase3Form, BusquedaForm
from .models import Clase1, Clase2, Clase3

def insertar_datos(request):
    if request.method == 'POST':
        form1 = Clase1Form(request.POST)
        form2 = Clase2Form(request.POST)
        form3 = Clase3Form(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
            return redirect('home')
    else:
        form1 = Clase1Form()
        form2 = Clase2Form()
        form3 = Clase3Form()
    return render(request, 'insertar_datos.html', {'form1': form1, 'form2': form2, 'form3': form3})

def buscar_datos(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            resultados_clase1 = Clase1.objects.filter(campo1__icontains=busqueda)
            resultados_clase2 = Clase2.objects.filter(campo3__icontains=busqueda)
            resultados_clase3 = Clase3.objects.filter(campo5__icontains=busqueda)
            return render(request, 'resultados_busqueda.html', {'resultados_clase1': resultados_clase1, 'resultados_clase2': resultados_clase2, 'resultados_clase3': resultados_clase3})
    else:
        form = BusquedaForm()
    return render(request, 'buscar_datos.html', {'form': form})

def home(request):
    return render(request, 'base.html')
