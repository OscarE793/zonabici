from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Bicicleta

class BicicletaListView(LoginRequiredMixin, ListView):
    model = Bicicleta
    template_name = 'bicicletas/lista_bicicletas.html'
    context_object_name = 'bicicletas'

    def get_queryset(self):
        return Bicicleta.objects.filter(usuario=self.request.user)

class BicicletaCreateView(LoginRequiredMixin, CreateView):
    model = Bicicleta
    fields = ['marca', 'color', 'serial']
    template_name = 'bicicletas/crear_bicicleta.html'
    success_url = reverse_lazy('bicicletas:lista_bicicletas')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
