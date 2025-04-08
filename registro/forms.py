from django import forms
from .models import RegistroMovimiento
from bicicletas.models import Bicicleta

class RegistroMovimientoForm(forms.ModelForm):
    class Meta:
        model = RegistroMovimiento
        fields = ['bicicleta', 'tipo_movimiento', 'observaciones']

    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)
        if usuario:
            self.fields['bicicleta'].queryset = Bicicleta.objects.filter(usuario=usuario)
