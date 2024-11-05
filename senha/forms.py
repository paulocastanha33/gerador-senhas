# senha/forms.py
from django import forms

class GeradorSenhaForm(forms.Form):
    comprimento = forms.IntegerField(label="Comprimento da Senha", min_value=4, max_value=64, initial=12)
    incluir_maiusculas = forms.BooleanField(label="Incluir Letras Maiúsculas", required=False, initial=True)
    incluir_minusculas = forms.BooleanField(label="Incluir Letras Minúsculas", required=False, initial=True)
    incluir_numeros = forms.BooleanField(label="Incluir Números", required=False, initial=True)
    incluir_simbolos = forms.BooleanField(label="Incluir Símbolos", required=False, initial=True)
