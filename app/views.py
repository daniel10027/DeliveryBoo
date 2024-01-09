from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .models import Colis
from .forms import ColisForm, CodeColisForm

def colis_list(request):
    colis_list = Colis.objects.all()
    return render(request, 'colis_list.html', {'colis_list': colis_list})

class ColisCreateView(CreateView):
    model = Colis
    form_class = ColisForm
    template_name = 'colis_form.html'
    success_url = reverse_lazy('colis_list')

class ColisUpdateView(UpdateView):
    model = Colis
    form_class = ColisForm
    template_name = 'colis_form.html'
    success_url = reverse_lazy('colis_list')

def recherche_colis(request):
    if request.method == 'POST':
        form = CodeColisForm(request.POST)
        if form.is_valid():
            code_colis = form.cleaned_data['code_colis']
            try:
                colis = Colis.objects.get(code=code_colis)
                return render(request, 'etat.html', {'colis': colis, 'form': CodeColisForm()})
            except Colis.DoesNotExist:
                message = "Aucun colis ne correspond au code saisi."
                return render(request, 'etat.html', {'form': form, 'message': message})
    else:
        form = CodeColisForm()
    return render(request, 'etat.html', {'form': form})