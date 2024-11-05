# senha/views.py
import random
import string
from django.shortcuts import render
from .forms import GeradorSenhaForm

def gerar_senha(request):
    senha_gerada = ""
    if request.method == "POST":
        form = GeradorSenhaForm(request.POST)
        if form.is_valid():
            comprimento = form.cleaned_data['comprimento']
            incluir_maiusculas = form.cleaned_data['incluir_maiusculas']
            incluir_minusculas = form.cleaned_data['incluir_minusculas']
            incluir_numeros = form.cleaned_data['incluir_numeros']
            incluir_simbolos = form.cleaned_data['incluir_simbolos']

            caracteres = ""
            if incluir_maiusculas:
                caracteres += string.ascii_uppercase
            if incluir_minusculas:
                caracteres += string.ascii_lowercase
            if incluir_numeros:
                caracteres += string.digits
            if incluir_simbolos:
                caracteres += string.punctuation

            if caracteres:
                senha_gerada = ''.join(random.choice(caracteres) for _ in range(comprimento))
            else:
                senha_gerada = "Escolha ao menos um tipo de caractere."
    else:
        form = GeradorSenhaForm()

    return render(request, 'senha/gerar_senha.html', {'form': form, 'senha_gerada': senha_gerada})
