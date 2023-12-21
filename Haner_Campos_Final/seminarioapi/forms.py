from django import forms
from seminarioapi import models

class InscritoForm(forms.ModelForm):
    class Meta:
        model = models.Inscrito
        fields = ['nombre', 'telefono', 'fechaInscripcion', 'institucion', 'horaInscripcion', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaInscripcion': forms.DateInput(attrs={'class': 'form-control'}),
            'institucion': forms.Select(attrs={'class': 'form-control'}),
            'horaInscripcion': forms.TimeInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super(InscritoForm, self).__init__(*args, **kwargs)
            self.fields['institucion'].choices = [(institucion.id, institucion.nombre) for institucion in models.Institucion.objects.all()]

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = models.Institucion
        fields = ['nombre', 'direccion', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
