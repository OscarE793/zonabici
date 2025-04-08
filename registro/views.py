from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import RegistroMovimiento
from .forms import RegistroMovimientoForm

class RegistroMovimientoCreateView(LoginRequiredMixin, CreateView):
    model = RegistroMovimiento
    form_class = RegistroMovimientoForm
    template_name = 'registro/registrar_movimiento.html'
    success_url = reverse_lazy('registro:historial')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs

class HistorialMovimientosView(LoginRequiredMixin, ListView):
    model = RegistroMovimiento
    template_name = 'registro/historial.html'
    context_object_name = 'movimientos'

    def get_queryset(self):
        return RegistroMovimiento.objects.filter(bicicleta__usuario=self.request.user).order_by('-fecha_hora')
