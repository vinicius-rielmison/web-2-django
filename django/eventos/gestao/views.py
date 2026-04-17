from django.shortcuts import render, redirect
from .forms import EventoForm

eventos = []

def home(request):
    return render(request, 'home.html', {'eventos': eventos})


def novo(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        
        if form.is_valid():
            evento = form.cleaned_data['evento']
            local = form.cleaned_data['local']
            
            eventos.append({
                'evento': evento,
                'local': local
            })
            
            return redirect('home')
    
    else:
        form = EventoForm()

    return render(request, 'novo.html', {'form': form})
# Create your views here.
