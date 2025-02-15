from django.shortcuts import render, redirect
from .models import Pacientes
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants


def pacientes(request):
    if request.method == "GET":
        pacientes_list = Pacientes.objects.all()
        return render(request, 'pacientes.html', {'queixas': Pacientes.queixa_choices, 'pacientes': pacientes_list})
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request, constants.ERROR, 'O campo nome e foto são obrigatórios')
            return redirect('pacientes')

        paciente = Pacientes(
            nome=nome,
            email=email,
            telefone=telefone,
            queixa=queixa,
            foto=foto
        )
        paciente.save()

        messages.add_message(request, constants.SUCCESS, 'Paciente adicionado com sucesso')
        return redirect('pacientes')
