from django import forms

class EventoForm(forms.Form):
    evento = forms.CharField(label='Evento')
    local = forms.CharField(label='Local')